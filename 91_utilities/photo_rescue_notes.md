# Accidental Movie Photo Rescue

This folder now has a repeatable converter for turning accidental `.mov` or `.mp4` clips into JPEG images.

Your iPad folder is:

```text
C:\Users\pkeen\2025_BHS\ipad
```

That folder currently appears to contain 401 `.MOV` files and a matching `HEIC` folder with 401 still images. This looks like an iPad Live Photo export: the `.HEIC` files are likely the intended still photos, and the `.MOV` files are the short motion clips.

## What It Does

- Looks through a source folder for videos.
- Exports one or two JPEG frames from each video.
- Names each image with the video date and original filename.
- Sets each JPEG's created and modified dates to match the original video file.
- Saves all exported images into a separate folder.

## How To Run It

Open PowerShell and run:

```powershell
.\video_frame_exporter.ps1 -SourceFolder "C:\path\to\your\videos" -OutputFolder "C:\path\to\exported\images" -FramesPerVideo 2
```

For your iPad folder, run:

```powershell
.\run_ipad_frame_export.ps1
```

## If It Says ffmpeg Is Missing

The converter uses `ffmpeg`, a standard video tool, to pull frames from videos. Install it once, then rerun:

```powershell
.\run_ipad_frame_export.ps1
```

After the JPEGs are exported, the output folder can be searched and sorted by date/name while you choose images for the principal presentation.
