<# Run approved E007 once in the existing audited image; change no host settings. #>
[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$expectedImageId = 'sha256:6731a5b19ee38fc98d58f3e84d47bceb2c8a6d1f69d37729c0c8352946f04f5c'
$gitRoot = & git -C $projectRoot rev-parse --show-toplevel
if ($LASTEXITCODE -ne 0 -or (Resolve-Path -LiteralPath $gitRoot.Trim()).Path -ne $projectRoot) { throw 'Project Git root mismatch.' }
$dirty = @(& git -C $projectRoot status --porcelain=v1 --untracked-files=all)
if ($LASTEXITCODE -ne 0 -or $dirty.Count -ne 0) { throw 'Commit approved implementation first; clean tree required.' }
$revision = & git -C $projectRoot rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or $revision.Trim() -cnotmatch '^[a-f0-9]{40}$') { throw 'Exact revision unavailable.' }
$imageId = & docker image inspect map-misconceptions:e001 --format '{{.Id}}'
if ($LASTEXITCODE -ne 0 -or $imageId.Trim() -cne $expectedImageId) { throw 'Audited image unavailable. No automatic pull/build.' }
$names = @(& docker container ls --all --format '{{.Names}}')
if ($LASTEXITCODE -ne 0 -or $names -contains 'responsible-ai-math-e007') { throw 'Cannot confirm safe single run.' }
$outputDir = Join-Path $projectRoot 'artifacts/e007'
foreach ($candidate in @($projectRoot, (Join-Path $projectRoot 'artifacts'), $outputDir)) {
    if (Test-Path -LiteralPath $candidate) {
        $item = Get-Item -LiteralPath $candidate -Force
        if (-not $item.PSIsContainer -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'Project/artifact paths must be real directories.' }
    }
}
foreach ($name in @('attempt.json','results.json','failure.json')) {
    if (Test-Path -LiteralPath (Join-Path $outputDir $name)) { throw 'Existing E007 attempt; no silent rerun.' }
}
if (-not (Test-Path -LiteralPath $outputDir)) { $null = New-Item -ItemType Directory -Path $outputDir }
if ((Resolve-Path -LiteralPath $outputDir).Path -ne (Join-Path $projectRoot 'artifacts\e007')) { throw 'Output directory outside expected project scope.' }
$dockerArgs = @('run','--rm','--pull','never','--name','responsible-ai-math-e007',
    '--network','none','--read-only','--tmpfs','/tmp:rw,nosuid,nodev',
    '--user','10001:10001','--cap-drop','ALL','--security-opt','no-new-privileges',
    '-e','PYTHONDONTWRITEBYTECODE=1','-e','PYTHONUNBUFFERED=1','-e','PYTHONPATH=/workspace/src',
    '-e','PYTHONHASHSEED=20260831','-e','OPENBLAS_NUM_THREADS=1','-e','OMP_NUM_THREADS=1','-e','MKL_NUM_THREADS=1',
    '--mount',"type=bind,source=$projectRoot,target=/workspace,readonly",
    '--mount',"type=bind,source=$outputDir,target=/workspace/artifacts/e007",
    '--workdir','/workspace',$expectedImageId,'python','scripts/run_e007_threshold_transfer.py',
    '--git-revision',$revision.Trim(),'--image-id',$expectedImageId)
Write-Host "Starting locked E007 at $($revision.Trim()). Only artifacts/e007 is writable."
& docker @dockerArgs
exit $LASTEXITCODE
