$sourceFolder = "C:\Users\pkeen\2025_BHS\ipad"
$outputFolder = Join-Path $PSScriptRoot "ipad_JPEG_frames"

.\video_frame_exporter.ps1 `
    -SourceFolder $sourceFolder `
    -OutputFolder $outputFolder `
    -FramesPerVideo 2 `
    -FirstFrameSeconds 0.5 `
    -SecondFramePercent 50
