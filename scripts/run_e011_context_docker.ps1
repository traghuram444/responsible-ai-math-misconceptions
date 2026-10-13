[CmdletBinding()]
param([Parameter(Mandatory=$true)][ValidateSet('E011','E012')][string]$Experiment)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$lock = Get-Content -LiteralPath (Join-Path $projectRoot 'experiments/e011_e012_lock.json') -Raw | ConvertFrom-Json
$imageId = & docker image inspect map-modeling:e011 --format '{{.Id}}'
if ($LASTEXITCODE -ne 0 -or $imageId.Trim() -cne $lock.docker_image_id) { throw 'Locked modeling image unavailable.' }
$dirty = @(& git -C $projectRoot status --porcelain=v1 --untracked-files=all)
if ($LASTEXITCODE -ne 0 -or $dirty.Count -ne 0) { throw 'Clean committed plan required.' }
$revision = (& git -C $projectRoot rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $revision -cnotmatch '^[a-f0-9]{40}$') { throw 'Revision unavailable.' }
$outputDir = Join-Path $projectRoot ('artifacts/' + $Experiment.ToLowerInvariant())
foreach ($candidate in @($projectRoot, (Join-Path $projectRoot 'artifacts'), $outputDir)) {
    if (Test-Path -LiteralPath $candidate) {
        $item = Get-Item -LiteralPath $candidate -Force
        if (-not $item.PSIsContainer -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'Real directories required.' }
    }
}
foreach ($name in @('attempt.json','results.json','failure.json')) {
    if (Test-Path -LiteralPath (Join-Path $outputDir $name)) { throw 'Existing attempt; no automatic retry.' }
}
if (-not (Test-Path -LiteralPath $outputDir)) { $null = New-Item -ItemType Directory -Path $outputDir }
$resolved = (Resolve-Path -LiteralPath $outputDir).Path
if ($resolved -ne [IO.Path]::GetFullPath($outputDir)) { throw 'Unexpected output path.' }
$dockerArgs = @('run','--rm','--pull','never','--name',('responsible-ai-math-' + $Experiment.ToLowerInvariant()),
    '--network','none','--read-only','--tmpfs','/tmp:rw,nosuid,nodev','--user','10001:10001',
    '--cap-drop','ALL','--security-opt','no-new-privileges','-e','PYTHONHASHSEED=20260831',
    '--mount',"type=bind,source=$projectRoot,target=/workspace,readonly",
    '--mount',"type=bind,source=$outputDir,target=/workspace/artifacts/$($Experiment.ToLowerInvariant())",
    '--workdir','/workspace',$imageId.Trim(),'python','scripts/run_e011_context.py',
    '--experiment',$Experiment,'--git-revision',$revision,'--image-id',$imageId.Trim())
if ($Experiment -eq 'E012') {
    $reference = Join-Path $projectRoot 'results/E011_aggregates.json'
    if (-not (Test-Path -LiteralPath $reference)) { throw 'Published E011 required.' }
    $dockerArgs += @('--e011-sha',(Get-FileHash -LiteralPath $reference -Algorithm SHA256).Hash.ToLowerInvariant())
}
Write-Host "Starting $Experiment at $revision; only its new artifact directory is writable."
& docker @dockerArgs
exit $LASTEXITCODE
