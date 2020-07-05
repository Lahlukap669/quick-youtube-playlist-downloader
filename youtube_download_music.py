import os
import shutil

try:
  os.system('pip install youtube_dl --upgrade')
  import youtube_dl
except ImportError:
  print("Trying to Install required module: youtube_dl\n")
  os.system('python -m pip install youtube_dl')


try:
  from ffmpy import FFmpeg
except ImportError:
  print("Trying to Install required module: ffmpy\n")
  os.system('python -m pip install ffmpy')


def download_song(song_url, path, ime):
      with youtube_dl.YoutubeDL() as ydl:
          try:
            info_dict = ydl.extract_info(song_url, download=True)
          except:
              pass
      
      if os.path.exists(path + "/" + ime)==False:
            os.mkdir(path + "/" + ime)
      
      for file in os.listdir('.'):
            if not file.endswith('py') and not file.endswith('md') and not file.endswith('spec') and not file.endswith('exe'):
                  try:
                        filename = file.split(".")[0].encode("ascii", errors="ignore").decode()
                        d = os.getcwd()
                        ff = FFmpeg(executable='ff/ffmpeg/bin/ffmpeg.exe',inputs={file: None}, outputs={path + "/" + ime + "/" + filename + ".mp3": None})
                        ff.run()
                        os.remove(file)
                  except:
                        pass

##      for file in os.listdir('.'):
 ##           if not file.endswith('py') and not file.endswith('md') and not file.endswith('spec') and not file.endswith('exe'):
 ##                 os.remove(file)
