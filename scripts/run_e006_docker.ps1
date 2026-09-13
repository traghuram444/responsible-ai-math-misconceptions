<#
.SYNOPSIS
Run the approved E006 once, in the already-installed audited Docker image.
.DESCRIPTION
Does not pull/build an image, install packages, or change host configuration.
The repository is mounted read-only; only artifacts/e006 is writable.
#>
[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$imageTag = 'map-misconceptions:e001'
$expectedImageId = 'sha256:6731a5b19ee38fc98d58f3e84d47bceb2c8a6d1f69d37729c0c8352946f04f5c'
$containerName = 'responsible-ai-math-e006'

$gitRoot = & git -C $projectRoot rev-parse --show-toplevel
if ($LASTEXITCODE -ne 0) { throw 'Cannot establish the project Git root.' }
if ((Resolve-Path -LiteralPath $gitRoot.Trim()).Path -ne $projectRoot) {
    throw 'Launcher must be inside the project repository, not a nested unrelated directory.'
}
$dirtyFiles = @(& git -C $projectRoot status --porcelain=v1 --untracked-files=all)
if ($LASTEXITCODE -ne 0) { throw 'Cannot verify the project Git working tree.' }
if ($dirtyFiles.Count -ne 0) {
    throw 'Commit the reviewed E006 implementation first; the project Git tree must be clean.'
}
$revision = & git -C $projectRoot rev-parse --verify HEAD
if ($LASTEXITCODE -ne 0) { throw 'Cannot identify the pre-run Git revision.' }
$revision = $revision.Trim()
if ($revision -cnotmatch '^[a-f0-9]{40}$') { throw 'A full 40-character Git revision is required.' }

$imageId = & docker image inspect $imageTag --format '{{.Id}}'
if ($LASTEXITCODE -ne 0) { throw 'The audited Docker image is unavailable; no automatic pull/build is allowed.' }
$imageId = $imageId.Trim()
if ($imageId -cne $expectedImageId) {
    throw 'Installed image differs from the audited E006 image. Stop; do not substitute or rebuild it.'
}
$containerNames = @(& docker container ls --all --format '{{.Names}}')
if ($LASTEXITCODE -ne 0) { throw 'Cannot check for an existing E006 container.' }
if ($containerNames -contains $containerName) {
    throw 'An E006 container already exists. Refusing a duplicate run or container removal.'
}

$artifactRoot = Join-Path $projectRoot 'artifacts'
$outputDir = Join-Path $artifactRoot 'e006'
foreach ($targetPath in @($projectRoot, $artifactRoot, $outputDir)) {
    if (Test-Path -LiteralPath $targetPath) {
        $targetItem = Get-Item -LiteralPath $targetPath -Force
        if (-not $targetItem.PSIsContainer -or
            ($targetItem.Attributes -band [System.IO.FileAttributes]::ReparsePoint)) {
            throw 'Project/output directories must be real directories, not links or files.'
        }
    }
}
if (-not (Test-Path -LiteralPath $artifactRoot -PathType Container)) {
    throw 'The existing project artifacts directory is required for frozen input/reference files.'
}
$resolvedArtifactRoot = (Resolve-Path -LiteralPath $artifactRoot).Path
if ($resolvedArtifactRoot -ne (Join-Path $projectRoot 'artifacts')) {
    throw 'Artifact directory is outside the intended project scope.'
}
foreach ($finalName in @('attempt.json', 'results.json', 'failure.json')) {
    if (Test-Path -LiteralPath (Join-Path $outputDir $finalName)) {
        throw 'An E006 attempt lock, result, or failure is already recorded. Refusing rerun or overwrite.'
    }
}
if (-not (Test-Path -LiteralPath $outputDir -PathType Container)) {
    # This is the sole host filesystem mutation performed by this launcher.
    $null = New-Item -ItemType Directory -Path $outputDir
}

$dockerArgs = @(
    'run', '--rm', '--pull', 'never', '--name', $containerName,
    '--network', 'none', '--read-only', '--tmpfs', '/tmp:rw,nosuid,nodev',
    '--user', '10001:10001', '--cap-drop', 'ALL', '--security-opt', 'no-new-privileges',
    '-e', 'PYTHONDONTWRITEBYTECODE=1', '-e', 'PYTHONUNBUFFERED=1',
    '-e', 'PYTHONPATH=/workspace/src', '-e', 'PYTHONHASHSEED=20260831',
    '-e', 'OPENBLAS_NUM_THREADS=1', '-e', 'OMP_NUM_THREADS=1', '-e', 'MKL_NUM_THREADS=1',
    '--mount', "type=bind,source=$projectRoot,target=/workspace,readonly",
    '--mount', "type=bind,source=$outputDir,target=/workspace/artifacts/e006",
    '--workdir', '/workspace', $imageId,
    'python', 'scripts/run_e006_selective.py', '--git-revision', $revision, '--image-id', $imageId
)
Write-Host "Starting approved E006 at commit $revision; fixed image $imageId."
Write-Host 'Only project artifacts/e006 is writable. No automatic rerun is performed.'
& docker @dockerArgs
exit $LASTEXITCODE
