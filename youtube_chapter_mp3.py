"""Extract audio for each chapter of the video and download it as a separate mp3 file.

Once you run the script, input the link of Youtube videos THAT HAVE CHAPTERS. 

This script is intended for Youtube videos with chapters, so I do not know what will happen for non-chaptered videos.

There is no exception handler included in this script, so don't test the behavior by putting erroneous inputs. 

Modify the parts with comments to configure settings like audio quality, format, download path, etc. 
"""
import yt_dlp
import os

def download_audio(LINK):
    ydl_opts = {
        'format': 'mp3/bestaudio/best',
        'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'nopostoverwrites': False,
          'preferredcodec': 'mp3',  # set the output file's format to mp3
          'preferredquality': '320',  # set audio bit rate to 320kbps 
        },
        {
          'key': 'FFmpegSplitChapters',
          'force_keyframes': False,
        }],
        'outtmpl': {'chapter': "D:\\logan\\Media\\음악\\%(title)s - %(section_title)s.%(ext)s"}, # set the download path
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