[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$lock = Get-Content -LiteralPath (Join-Path $projectRoot 'experiments/e017_lock.json') -Raw | ConvertFrom-Json
$imageId = (& docker image inspect map-modeling:e011 --format '{{.Id}}').Trim()
if ($LASTEXITCODE -ne 0 -or $imageId -cne $lock.docker_image_id) { throw 'Locked image required.' }
$dirty = @(& git -C $projectRoot status --porcelain=v1 --untracked-files=all)
if ($LASTEXITCODE -ne 0 -or $dirty.Count -ne 0) { throw 'Clean committed plan required.' }
$revision = (& git -C $projectRoot rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $revision -cnotmatch '^[a-f0-9]{40}$') { throw 'Exact revision required.' }
$outputDir = Join-Path $projectRoot 'artifacts/e017_attempt01'
foreach ($candidate in @($projectRoot,(Join-Path $projectRoot 'artifacts'))) {
    $item = Get-Item -LiteralPath $candidate -Force
    if (-not $item.PSIsContainer -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'Real directories required.' }
}
if (Test-Path -LiteralPath $outputDir) { throw 'Attempt exists; no overwrite or automatic retry.' }
foreach ($entry in $lock.private_evidence.PSObject.Properties) {
    $digest = (Get-FileHash -LiteralPath (Join-Path $projectRoot $entry.Name) -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($digest -cne $entry.Value) { throw 'Historical attempt changed.' }
}
$null = New-Item -ItemType Directory -Path $outputDir
$dockerArgs = @('run','--rm','--pull','never','--name','responsible-ai-math-e017-attempt01',
    '--network','none','--read-only','--tmpfs','/tmp:rw,nosuid,nodev','--user','10001:10001',
    '--cap-drop','ALL','--security-opt','no-new-privileges','-e','PYTHONHASHSEED=20260831',
    '--mount',"type=bind,source=$projectRoot,target=/workspace,readonly",
    '--mount',"type=bind,source=$outputDir,target=/workspace/artifacts/e017_attempt01",
    '--workdir','/workspace',$imageId,'python','scripts/run_e017.py','--git-revision',$revision,'--image-id',$imageId)
Write-Host "Starting approved E017 at $revision; prior attempts remain read-only."
& docker @dockerArgs
exit $LASTEXITCODE
