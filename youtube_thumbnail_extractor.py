import yt_dlp
from yt_dlp.postprocessor import FFmpegPostProcessor
FFmpegPostProcessor._ffmpeg_location.set(R'C:\\Users\\logan\\Desktop\\Delve\\Cyber\\Project\\UNCLASSIFIED\\MacGyver\\yt-dlp-related\\ffmpeg\\bin\\ffmpeg.exe')  # ffmpeg location

def download_thumbnail(link):
    ydl_opts = {
        'postprocessors': [{
          'format': 'jpg',  # set image format
          'key': 'FFmpegThumbnailsConvertor',
          'when': 'before_dl'
        }],
        'outtmpl': "M:\\Other computers\\My PC\\음악\\Spotify Album Cover\\%(title)s.%(ext)s",  # set output path and filename
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
  