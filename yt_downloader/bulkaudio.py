import yt_dlp
import os

# -----------------------------
# Read URLs from a file or input
# -----------------------------
choice = input("Download from (1) Text File or (2) Manual Input? : ")

urls = []

if choice == "1":
    file_path = input("Enter Text File Path: ")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        print("File not found!")
        exit()

elif choice == "2":
    url_input = input("Enter URLs separated by comma: ")
    urls = [u.strip() for u in url_input.split(",") if u.strip()]

else:
    print("Invalid Choice!")
    exit()

# -----------------------------
# Download Logic
# -----------------------------
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '0',
    }],
    'ffmpeg_location': r"C:\vs_code_programs\yt_downloader\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin",
    'outtmpl': r"E:/Download/%(title)s-%(id)s.%(ext)s",  # Use raw string
    'ignoreerrors': True,  # Continue even if one fails
}

print(f"\nStarting Download for {len(urls)} items...\n")

failed = []

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for url in urls:
        print(f"Downloading: {url}")
        try:
            ydl.download([url])
        except Exception as e:
            print(f"❌ Failed: {url} — {e}")
            failed.append(url)

print("\n✔ Download Completed!")

if failed:
    print("\n⚠ Failed Downloads:")
    for f in failed:
        print(f)
