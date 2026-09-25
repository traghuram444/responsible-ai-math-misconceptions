<# Read-only E007 terminal monitor. No idle recurring monitor. #>
[CmdletBinding()]
param([switch]$Once)
$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$statusFile = Join-Path $projectRoot 'artifacts/e007/live_status.json'
if (-not (Test-Path -LiteralPath $statusFile)) { Write-Host 'No E007 run status. Monitor not started.'; exit 0 }
$image = 'sha256:6731a5b19ee38fc98d58f3e84d47bceb2c8a6d1f69d37729c0c8352946f04f5c'
$argsList = @('run','--rm','--pull','never','--network','none','--read-only',
    '--user','10001:10001','--cap-drop','ALL','--security-opt','no-new-privileges',
    '-e','PYTHONDONTWRITEBYTECODE=1','-e','PYTHONUNBUFFERED=1','-e','PYTHONPATH=/workspace/src',
    '--mount',"type=bind,source=$projectRoot,target=/workspace,readonly",'--workdir','/workspace')
if (-not $Once -and -not [Console]::IsOutputRedirected) { $argsList += '--tty' }
# The existing renderer reads the experiment ID from the selected status file.
$argsList += @($image,'python','scripts/monitor_e006.py','--status-file','artifacts/e007/live_status.json')
if ($Once) { $argsList += '--once' }
& docker @argsList
exit $LASTEXITCODE
