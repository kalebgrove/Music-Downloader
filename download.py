import yt_dlp

# Options for yt-dlp
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',  # Output filename format
}

# Function to download video
def download_video(url):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Read video URLs from the text file
with open('name-of-urls-txt-file', 'r') as file:
    video_urls = file.readlines()

# Download each video
for url in video_urls:
    url = url.strip()  # Remove any leading/trailing whitespace
    if url:  # Ensure the line is not empty
        download_video(url)
