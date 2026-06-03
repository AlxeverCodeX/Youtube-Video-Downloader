import streamlit as st
import yt_dlp
from pathlib import Path

st.set_page_config(page_title="YouTube Downloader", page_icon="🎥")

st.title("🎥 Simple YouTube Downloader")
st.write("Paste a video link, choose quality, and download.")

url = st.text_input("Paste YouTube URL")

quality = st.selectbox(
    "Choose quality",
    ["Best", "1080p", "720p", "480p", "360p", "Audio only"]
)

download_folder = Path("downloads")
download_folder.mkdir(exist_ok=True)

def get_format(q):
    if q == "Best":
        return "bestvideo+bestaudio/best"
    if q == "Audio only":
        return "bestaudio/best"

    height = q.replace("p", "")
    return f"bestvideo[height<={height}]+bestaudio/best[height<={height}]"

if st.button("Download"):
    if not url:
        st.error("Please paste a YouTube URL first.")
    else:
        with st.spinner("Downloading..."):
            try:
                options = {
                    "format": get_format(quality),
                    "outtmpl": str(download_folder / "%(title)s.%(ext)s"),
                    "merge_output_format": "mp4",
                }

                if quality == "Audio only":
                    options["postprocessors"] = [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                    }]

                with yt_dlp.YoutubeDL(options) as ydl:
                    ydl.download([url])

                st.success("Download complete! Check the downloads folder.")

            except Exception as e:
                st.error(f"Error: {e}")