import yt_dlp

try:
    url = input("Enter the YouTube URL: ")

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]/best[ext=mp4]',  
        'outtmpl': '/Users/aleks/Desktop/python/yt/%(title)s.%(ext)s',
        'noplaylist': True,  
        'merge_output_format': None,  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Downloading...")
        ydl.download([url])
        print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))
