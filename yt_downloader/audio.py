import yt_dlp
url_input=input("Enter Url: ")
url=[url.strip() for url in url_input.split(",") if url.strip()]

ydl_opts={
    'format':'bestaudio/best',
    'postprocessors': [{
    'key':'FFmpegExtractAudio',
    'preferredcodec':'mp3',
    'preferredquality':'0',
    }],
    'ffmpeg_location': r"C:\vs_code_programs\yt_downloader\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin",
    'outtmpl':r'E:/Download/%(title)s-%(id)s.%(ext)s'
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)

print("Download Completed..")