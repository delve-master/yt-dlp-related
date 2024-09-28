import yt_dlp
import os
from yt_dlp.postprocessor import FFmpegPostProcessor
FFmpegPostProcessor._ffmpeg_location.set(R'C:\\Users\\logan\\Desktop\\Delve\\Cyber\\Project\\UNCLASSIFIED\\MacGyver\\yt-dlp-related\\ffmpeg\\bin\\ffmpeg.exe')  # set ffmpeg location

def download_audio(LINK):
    ydl_opts = {
        'format': 'mp3/bestaudio/best',
        'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'nopostoverwrites': False,
          'preferredcodec': 'mp3',  # set output file's format to mp3
          'preferredquality': '320',  # set audio bit rate to 320kbps 
        },
        {
          'key': 'FFmpegSplitChapters',
          'force_keyframes': False,
        }],
        'outtmpl': {'chapter': "M:\\Other computers\\My PC\\음악\\%(title)s - %(section_title)s.%(ext)s"}, # set download path
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:  
        info_dict = ydl.extract_info(LINK, download = True)
        print("Removing the original file...")
        os.remove(info_dict['requested_downloads'][0]['filepath'])  # if you want to keep the original source, exclude this line
        print("Successfully Downloaded - see local Spotify folder")

if __name__ == "__main__":
  while True:
    LINK = input("Type 'exit' to quit.\nYoutube link for \"split\" mp3 extraction: ")
    if LINK.lower() == "exit":
      exit()
    download_audio(LINK)