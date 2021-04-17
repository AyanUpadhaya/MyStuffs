import youtube_dl
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