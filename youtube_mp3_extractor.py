"""Extract audio for Youtube videos and download them as mp3 files.

Once you run the script, input the link of Youtube videos.

The link could be for BOTH single videos and playlists with multiple videos. 

There is no exception handler included in this script, so don't test the behavior by putting erroneous inputs. 

Modify the parts with comments to configure settings like audio quality, format, download path, etc. 
"""
import yt_dlp

def download_audio(link):
    ydl_opts = {
        "format": "mp3/bestaudio/best",
        "ignoreerrors": True,
        "postprocessors": [
            {
              "key": "FFmpegExtractAudio",
              "nopostoverwrites": False,
              "preferredcodec": "mp3",  # set the output file's format to mp3
              "preferredquality": "320",  # set audio bit rate to 320kbps
            },
            {
              "key": "FFmpegConcat", 
              "only_multi_video": True, 
              "when": "playlist"
            }
        ],
        "outtmpl": "D:\\logan\\Media\\음악\\%(title)s.%(ext)s", # set the download path
    }

    with yt_dlp.YoutubeDL(ydl_opts) as video:  
        info_dict = video.extract_info(link, download=False)
        video_title = info_dict["title"]
        print("MP3 for:" + video_title)
        video.download(link)
        print("Successfully Downloaded - see local Spotify folder")


if __name__ == "__main__":
    while True:
        link = input("Type 'exit' to quit.\nYoutube link for mp3 extraction: ")
        if link.lower() == "exit":
            exit()
        download_audio(link)
