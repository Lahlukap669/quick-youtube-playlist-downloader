import youtube_dl
import os
import shutil
from ffmpy import FFmpeg

def download_song(song_url):
      with youtube_dl.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(song_url, download=True)
      
      if os.path.exists(os.getcwd() + "/ff")==False:
            os.mkdir(os.getcwd() + "/ff")
      if os.path.exists(os.getcwd() + "/songs")==False:
            os.mkdir(os.getcwd() + "/songs")
      
      for file in os.listdir('.'):
            if not file.endswith('py'):
                  try:
                        filename = file.split(".")[0]
                        d = os.getcwd()
                        ff = FFmpeg(executable='ff/ffmpeg/bin/ffmpeg.exe',inputs={file: None}, outputs={"./songs/" + filename + ".mp3": None})
                        ff.run()
                  except:
                        pass

##      for file in os.listdir('.'):
##            if file.endswith('mp4') or file.endswith('webm') or file.endswith('mkv'):
##                  os.remove(file)

download_song(input("vnes link playlita: "))
