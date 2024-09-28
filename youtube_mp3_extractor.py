import yt_dlp
from yt_dlp.postprocessor import FFmpegPostProcessor
FFmpegPostProcessor._ffmpeg_location.set(R'C:\\Users\\logan\\Desktop\\Delve\\Cyber\\Project\\UNCLASSIFIED\\MacGyver\\yt-dlp-related\\ffmpeg\\bin\\ffmpeg.exe')  # ffmpeg location

def download_audio(link):
    ydl_opts = {
        "format": "mp3/bestaudio/best",
        "ignoreerrors": True,
        "postprocessors": [
            {
              "key": "FFmpegExtractAudio",
              "nopostoverwrites": False,
              "preferredcodec": "mp3",  # set output file's format to mp3
              "preferredquality": "320",  # set audio bit rate to 320kbps
            },
            {
              "key": "FFmpegConcat", 
              "only_multi_video": True, 
              "when": "playlist"
            }
        ],
        "outtmpl": "M:\\Other computers\\My PC\음악\\%(title)s.%(ext)s", # set download path
    }

    with yt_dlp.YoutubeDL(ydl_opts) as video:  
        info_dict = video.extract_info(link, download=False)
        video_title = info_dict["title"]
        print("MP3 for:" + video_title)
        error_code = video.download(link)
        print('An error occurred; video failed to download' if error_code
              else 'Video successfully downloaded')


if __name__ == "__main__":
    while True:
        link = input("Type 'exit' to quit.\nYoutube link for mp3 extraction: ")
        if link.lower() == "exit":
            exit()
        download_audio(link)
