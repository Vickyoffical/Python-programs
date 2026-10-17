import yt_dlp
url_input=input("Enter Url: ")
url=[url.strip() for url in url_input.split(",") if url.strip()]

ydl_opts={
    'format':'best[height<=720]+bestaudio/best',
    'merge_output_format':'mp4',
    'ffmpeg_location': r"C:\yt_download\ffmpeg\bin\ffmpeg.exe",
    'outtmpl':r"E:/Download/%(title)s-%(id)s.%(ext)s"
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)

print("Download Completed..")