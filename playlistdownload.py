from pytube import Playlist, YouTube

p = Playlist("https://youtube.com/playlist?list=PLbpi6ZahtOH6rWreRZlNiUvfcoehrM1w0&si=HzQ07TY5L5LRFpsN")

print(f"Total videos found: {len(p.video_urls)}")

for url in p.video_urls:
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("Downloaded:", yt.title)
    except Exception as e:
        print("Error downloading:", e)
print("All downloads completed.")