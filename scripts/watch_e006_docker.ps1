<#
.SYNOPSIS
Read the E006 live monitor without modifying or interrupting the experiment.
.DESCRIPTION
Uses the existing audited image with no network and a read-only project mount.
Exits if the run is absent, stale, completed, or failed. No idle monitor persists.
#>
[CmdletBinding()]
param([switch]$Once)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$expectedImageId = 'sha256:6731a5b19ee38fc98d58f3e84d47bceb2c8a6d1f69d37729c0c8352946f04f5c'
$imageId = & docker image inspect 'map-misconceptions:e001' --format '{{.Id}}'
if ($LASTEXITCODE -ne 0) { throw 'The audited Docker image is unavailable; no pull/build will be attempted.' }
$imageId = $imageId.Trim()
if ($imageId -cne $expectedImageId) { throw 'Installed image differs from the audited E006 image.' }

$dockerArgs = @('run')
if (-not $Once -and -not [Console]::IsOutputRedirected) {
    # Allocate a terminal only for an interactive monitor, enabling screen redraw.
    $dockerArgs += '--tty'
}
$dockerArgs += @(
    '--rm', '--pull', 'never', '--network', 'none', '--read-only',
    '--user', '10001:10001', '--cap-drop', 'ALL', '--security-opt', 'no-new-privileges',
    '-e', 'PYTHONDONTWRITEBYTECODE=1', '-e', 'PYTHONUNBUFFERED=1', '-e', 'PYTHONPATH=/workspace/src',
    '--mount', "type=bind,source=$projectRoot,target=/workspace,readonly",
    '--workdir', '/workspace', $imageId,
    'python', 'scripts/monitor_e006.py', '--status-file', 'artifacts/e006/live_status.json'
)
if ($Once) { $dockerArgs += '--once' }
& docker @dockerArgs
exit $LASTEXITCODE
