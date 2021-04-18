import youtube_dl

import os

path='C:/Users/ayanU/Downloads'

os.chdir(path)

def downloader():
	url=input('Enter url:')
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])
	print('Want to download again?')
	user=input('>:')
	if user=='y':
		downloader()
	else:
		exit()


downloader()