# Youtube-Video-Downloader

A lightweight YouTube video downloader built with Python, Streamlit, yt-dlp, and FFmpeg. Users can paste a YouTube video URL, select their preferred quality, and download videos through a simple web interface.

## Features

* Download YouTube videos from a URL
* Select preferred video quality

  * Best Available
  * 1080p
  * 720p
  * 480p
  * 360p
* Download audio-only versions of videos
* Simple and clean Streamlit web interface
* Fast downloads powered by yt-dlp
* Automatic video/audio merging using FFmpeg

## Tech Stack

* Python
* Streamlit
* yt-dlp
* FFmpeg

## Project Structure

```text
youtube-downloader/
│
├── app.py
├── requirements.txt
├── packages.txt
├── downloads/
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-downloader.git

cd youtube-downloader
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install FFmpeg

This project requires FFmpeg to merge video and audio streams.

Windows:

```bash
winget install Gyan.FFmpeg
```

Verify installation:

```bash
ffmpeg -version
```

## Running the Application

```bash
python -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## How It Works

1. User enters a YouTube URL.
2. User selects a preferred quality.
3. yt-dlp retrieves the available video streams.
4. FFmpeg merges the video and audio streams when necessary.
5. The downloaded file is saved locally.

## Challenges Encountered

During development, several issues were encountered and resolved:

### Broken pip Installation

Issue:

```text
Fatal error in launcher
```

Solution:

Used Python's module installer directly:

```bash
python -m pip install streamlit yt-dlp
```

### Streamlit Command Not Found

Issue:

```text
streamlit: command not found
```

Solution:

Executed Streamlit through Python:

```bash
python -m streamlit run app.py
```

### FFmpeg Not Detected

Issue:

```text
ERROR: You have requested merging of multiple formats but ffmpeg is not installed.
```

Solution:

Installed FFmpeg and configured yt-dlp to locate the FFmpeg binary correctly.

### YouTube Format Merging

Issue:

High-quality downloads required separate video and audio streams.

Solution:

Integrated FFmpeg to merge streams into a single MP4 file.

## Future Improvements

* Download progress indicator
* Video metadata preview
* Direct browser downloads
* Download history tracking
* Multi-platform video support

## Learning Outcomes

This project provided hands-on experience with:

* Python package management
* Streamlit application development
* Video processing workflows
* yt-dlp integration
* FFmpeg configuration
* Debugging environment and dependency issues
* Building and deploying simple web applications

## Disclaimer

This project is intended for educational purposes and personal use. Users should ensure they have the necessary rights or permissions before downloading content from any platform.

