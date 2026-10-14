[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$lock = Get-Content -LiteralPath (Join-Path $projectRoot 'experiments/e012_attempt02_lock.json') -Raw | ConvertFrom-Json
$imageId = (& docker image inspect map-modeling:e011 --format '{{.Id}}').Trim()
if ($LASTEXITCODE -ne 0 -or $imageId -cne $lock.docker_image_id) { throw 'Locked image required.' }
$dirty = @(& git -C $projectRoot status --porcelain=v1 --untracked-files=all)
if ($LASTEXITCODE -ne 0 -or $dirty.Count -ne 0) { throw 'Clean committed amendment required.' }
$revision = (& git -C $projectRoot rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $revision -cnotmatch '^[a-f0-9]{40}$') { throw 'Exact revision required.' }
$artifacts = Join-Path $projectRoot 'artifacts'
$failed = Join-Path $artifacts 'e012'
$outputDir = Join-Path $artifacts 'e012_attempt02'
foreach ($candidate in @($projectRoot,$artifacts,$failed)) {
    $item = Get-Item -LiteralPath $candidate -Force
    if (-not $item.PSIsContainer -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'Real directories required.' }
}
if (Test-Path -LiteralPath $outputDir) { throw 'Attempt directory already exists; do not overwrite.' }
$failureRecord = Get-Content -LiteralPath (Join-Path $projectRoot 'results/E012_execution_failure.json') -Raw | ConvertFrom-Json
$names = @{attempt='attempt.json'; failure='failure.json'; terminal_status='live_status.json'}
foreach ($key in $names.Keys) {
    $actual = (Get-FileHash -LiteralPath (Join-Path $failed $names[$key]) -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -cne $failureRecord.source_sha256.$key) { throw 'Failed attempt changed.' }
}
$null = New-Item -ItemType Directory -Path $outputDir
$dockerArgs = @('run','--rm','--pull','never','--name','responsible-ai-math-e012-attempt02',
    '--network','none','--read-only','--tmpfs','/tmp:rw,nosuid,nodev','--user','10001:10001',
    '--cap-drop','ALL','--security-opt','no-new-privileges','-e','PYTHONHASHSEED=20260831',
    '--mount',"type=bind,source=$projectRoot,target=/workspace,readonly",
    '--mount',"type=bind,source=$failed,target=/workspace/artifacts/e012_failed_attempt01,readonly",
    '--mount',"type=bind,source=$outputDir,target=/workspace/artifacts/e012",
    '--workdir','/workspace',$imageId,'python','scripts/run_e012_attempt02.py',
    '--git-revision',$revision,'--image-id',$imageId)
Write-Host "Starting E012 attempt02 at $revision; failed attempt is read-only."
& docker @dockerArgs
exit $LASTEXITCODE
