#!/usr/bin/env python
import os
from mutagen.easyid3 import EasyID3
class mp3:
    def __init__(self,path):
        self.loc,self.name=os.path.split(path)
        self.file=EasyID3(path)

    def __del__(self):
        self.file.save()

class folder:
    def __init__(self,artist,album):
        root="/Users/ebakan/Music/iTunes/iTunes Media/Music/"
        self.fullpath=os.path.join(os.path.join(root, artist), album)
        mp3s=self.files()
        for mp3 in mp3s:
            self.modify(mp3)

    def files(self):
        return [mp3(os.path.join(path,file)) for path, dirs, files in os.walk(self.fullpath) for file in files]

    def modify(self,mp3):
	"""
	name=mp3.name
	dash=name.rindex("-")
	artist=name[dash+1:-4]
	title=name[3:dash]
	mp3.file['artist']=artist
	mp3.file['title']=title
	"""
	title=mp3.file['artist'][0]
	mp3.file['artist']=mp3.file['title'][0]
	mp3.file['title']=title
#mp3.file['tracknumber']=num
#mp3.file['title']=name

if __name__=='__main__':
    artist="Nujabes"
    album="First Collection"
    f=folder(artist,album)
