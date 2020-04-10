# pip install pytube
from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=oxpGjENMH4s').streams.first().download()
