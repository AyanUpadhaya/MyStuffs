import webbrowser

import datetime

current_time=datetime.datetime.now()
year=current_time.year
month=current_time.month
day=current_time.day
hour=current_time.hour 
minute=current_time.minute 
date=str(year)+"/"+str(month)+"/"+str(day)
time=str(hour)+":"+str(minute)

def searchYoutube():
	print("Enter your search:")

	keyword=input()

	search="https://www.youtube.com/results?search_query="+keyword

	print("Save history?")
	history=input()

	if history=='y':
		saveHistory(keyword,search)
	else:
		browser=webbrowser.open(search)


def saveHistory(keyword,search):
	browser=webbrowser.open(search)
	with open("browsehistory.txt","a") as file:
		file.write("Search title: "+keyword+"\n")
		file.write(str(search)+"\n")
		file.write(date+" "+time+"\n")
		print("saved!")
		print("Search again?")
		newsearch=input()
		if newsearch=='y':
			searchYoutube()
		else:
			exit()


searchYoutube()


