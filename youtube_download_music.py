import os
import shutil

try:
  import youtube_dl
except ImportError:
  print("Trying to Install required module: youtube_dl\n")
  os.system('python -m pip install youtube_dl')


try:
  from ffmpy import FFmpeg
except ImportError:
  print("Trying to Install required module: ffmpy\n")
  os.system('python -m pip install ffmpy')


def download_song(song_url):
      with youtube_dl.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(song_url, download=True)
      
      if os.path.exists(os.getcwd() + "/songs")==False:
            os.mkdir(os.getcwd() + "/songs")
      
      for file in os.listdir('.'):
            if not file.endswith('py') and not file.endswith('md') and not file.endswith('spec'):
                  try:
                        filename = file.split(".")[0]
                        d = os.getcwd()
                        ff = FFmpeg(executable='ff/ffmpeg/bin/ffmpeg.exe',inputs={file: None}, outputs={"./songs/" + filename + ".mp3": None})
                        ff.run()
                        os.remove(file)
                  except:
                        pass

##      for file in os.listdir('.'):
##            if file.endswith('mp4') or file.endswith('webm') or file.endswith('mkv'):
##                  os.remove(file)

download_song(input("playlist_url: "))
