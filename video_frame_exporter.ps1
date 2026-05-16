param(
    [Parameter(Mandatory = $true)]
    [string]$SourceFolder,

    [Parameter(Mandatory = $true)]
    [string]$OutputFolder,

    [ValidateSet(1, 2)]
    [int]$FramesPerVideo = 2,

    [double]$FirstFrameSeconds = 0.5,

    [double]$SecondFramePercent = 50,

    [int]$JpegQuality = 2
)

$ErrorActionPreference = "Stop"

function Resolve-Ffmpeg {
    $cmd = Get-Command ffmpeg -ErrorAction SilentlyContinue
    if ($cmd) {
        return $cmd.Source
    }

    $commonPaths = @(
        "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-*\bin\ffmpeg.exe",
        "$env:ProgramFiles\ffmpeg\bin\ffmpeg.exe",
        "$env:ProgramFiles(x86)\ffmpeg\bin\ffmpeg.exe"
    )

    foreach ($pathPattern in $commonPaths) {
        $match = Get-ChildItem -Path $pathPattern -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($match) {
            return $match.FullName
        }
    }

    throw "ffmpeg was not found. Install ffmpeg, then run this script again."
}

function Get-VideoDurationSeconds {
    param(
        [string]$FfmpegPath,
        [string]$VideoPath
    )

    $output = & $FfmpegPath -i $VideoPath 2>&1 | Out-String
    $durationMatch = [regex]::Match($output, "Duration:\s(?<hh>\d{2}):(?<mm>\d{2}):(?<ss>\d{2}(?:\.\d+)?)")
    if (-not $durationMatch.Success) {
        return $null
    }

    $hours = [double]$durationMatch.Groups["hh"].Value
    $minutes = [double]$durationMatch.Groups["mm"].Value
    $seconds = [double]$durationMatch.Groups["ss"].Value
    return ($hours * 3600) + ($minutes * 60) + $seconds
}

function Export-Frame {
    param(
        [string]$FfmpegPath,
        [string]$VideoPath,
        [double]$TimestampSeconds,
        [string]$ImagePath,
        [int]$Quality
    )

    & $FfmpegPath `
        -hide_banner `
        -loglevel error `
        -y `
        -ss $TimestampSeconds.ToString("0.###", [Globalization.CultureInfo]::InvariantCulture) `
        -i $VideoPath `
        -frames:v 1 `
        -q:v $Quality `
        $ImagePath
}

$source = Resolve-Path -LiteralPath $SourceFolder
$output = New-Item -ItemType Directory -Force -Path $OutputFolder
$ffmpeg = Resolve-Ffmpeg

$videos = Get-ChildItem -LiteralPath $source -File -Recurse |
    Where-Object { $_.Extension -in ".mov", ".MOV", ".mp4", ".MP4" } |
    Sort-Object LastWriteTime, Name

if (-not $videos) {
    Write-Host "No .mov or .mp4 files found in $source"
    exit 0
}

Write-Host "Found $($videos.Count) video file(s). Exporting JPEGs to $($output.FullName)"

$exported = 0
foreach ($video in $videos) {
    $duration = Get-VideoDurationSeconds -FfmpegPath $ffmpeg -VideoPath $video.FullName
    $timestamps = @($FirstFrameSeconds)

    if ($FramesPerVideo -eq 2 -and $duration) {
        $percentPoint = [Math]::Max(0.1, [Math]::Min($duration - 0.1, $duration * ($SecondFramePercent / 100)))
        $timestamps += $percentPoint
    }

    for ($i = 0; $i -lt $timestamps.Count; $i++) {
        $frameNumber = ($i + 1).ToString("00")
        $datePrefix = $video.LastWriteTime.ToString("yyyy-MM-dd_HHmmss")
        $imageName = "{0}_{1}_frame{2}.jpg" -f $datePrefix, $video.BaseName, $frameNumber
        $imagePath = Join-Path $output.FullName $imageName

        Export-Frame -FfmpegPath $ffmpeg -VideoPath $video.FullName -TimestampSeconds $timestamps[$i] -ImagePath $imagePath -Quality $JpegQuality

        if (Test-Path -LiteralPath $imagePath) {
            $image = Get-Item -LiteralPath $imagePath
            $image.CreationTime = $video.CreationTime
            $image.LastWriteTime = $video.LastWriteTime
            $image.LastAccessTime = $video.LastAccessTime
            $exported += 1
            Write-Host "Created $imageName"
        }
    }
}

Write-Host "Done. Created $exported JPEG file(s)."
