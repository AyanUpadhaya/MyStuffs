import webbrowser,os

import datetime


print("Enter your search:")

keyword=input()

search="https://www.youtube.com/results?search_query="+keyword

print("Save history?")
history=input()

current_time=datetime.datetime.now()
year=current_time.year
month=current_time.month
day=current_time.day
hour=current_time.hour 
min=current_time.minute 

date=str(year)+"/"+str(month)+"/"+str(day)
time=str(hour)+":"+str(min)

if history=='y':
	browser=webbrowser.open(search)
	with open("browsehistory.txt","a") as file:
		file.write("Search title: "+keyword+"\n")
		file.write(str(search)+"\n")
		file.write(date+" "+time+"\n")
		print("saved!")
else:
	browser=webbrowser.open(search)

