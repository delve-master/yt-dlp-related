"""Extract thumbnails for Youtube videos and download them as jpg files.

Once you run the script, input the link of Youtube videos.

There is no exception handler included in this script, so don't test the behavior by putting erroneous inputs. 

Modify the parts with comments to configure settings like the format, download path, etc. 
"""

import yt_dlp

def download_thumbnail(link):
    ydl_opts = {
        'postprocessors': [{
          'format': 'jpg',  # set the image format
          'key': 'FFmpegThumbnailsConvertor',
          'when': 'before_dl'
        }],
        'outtmpl': "D:\logan\Media\음악\Spotify Album Cover\%(title)s.%(ext)s",  # set the output path and filename
        'skip_download': True,  # skip downloading the video
        'writethumbnail': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        video_title = info_dict['title']
        print("Thumbnail for " + video_title)        
        ydl.download(link)
        print("Successfully Downloaded - see local Spotify Album folder")

if __name__ == "__main__":
  while True:
    link = input("Type 'exit' to quit.\nYoutube link for thumbnail extraction: ")   
    if link.lower() == "exit":
      exit()
    download_thumbnail(link)
  