import webbrowser
import datetime
import sqlite3
import os


class Console:
	def log(x):
		print(x)
	def get():
		x=input()
		return x

class Youtuber:
	def __init__(self,name,channel,keyname):
		self.name=name
		self.channel=channel
		self.keyname=keyname
		self.current_time=datetime.datetime.now()
		self.year=self.current_time.year
		self.month=self.current_time.month
		self.day=self.current_time.day
		self.hour=self.current_time.hour 
		self.minute=self.current_time.minute 
		self.date=str(self.year)+"/"+str(self.month)+"/"+str(self.day)
		self.timedata=str(self.hour)+":"+str(self.minute)
		self.keyword=''
		self.search=''

	def saveintoDB(self,keyword,search):
		con=sqlite3.connect('youTube.db')
		c=con.cursor()
		c.execute("INSERT INTO youtubers VALUES(?,?,?)",(self.keyname,keyword,search))
		con.commit()

	def browse(self):
		Console.log("Opening up {} YouTube channel...".format(self.name))
		webbrowser.open(self.channel)

	def saveInfo(self):
		Console.log("Save Name of the video:")
		self.keyword=Console.get()
		Console.log("Save Link of the video:")
		self.search=Console.get()
		self.youtubeHistory(self.keyword,self.search)
		

	def youtubeHistory(self,keyword,search):

		with open("browsehistory.txt","a") as file:
			file.write("Channel Name: "+self.name+'\n')
			file.write("Video title: "+keyword+"\n")
			file.write("Link: "+str(search)+"\n")
			file.write(self.date+" "+self.timedata+"\n")
			Console.log("saved!")
			Console.log("Enter a new link?")
			newsearch=Console.get()
			if newsearch=='y':
				self.saveInfo()
				self.saveintoDB(keyword,search)



kalle=Youtuber('Kall Hallden','https://www.youtube.com/c/KalleHallden/videos','kalle$')
tim=Youtuber('Tim','https://www.youtube.com/c/TechWithTim/videos','tim$')
kylie=Youtuber('Kylie Ying','https://www.youtube.com/c/YCubed/videos','kylie$')

Console.log(kalle.keyname)
Console.log(tim.keyname)
Console.log(kylie.keyname)
Console.log('-------------------')




def insertDatawithTable():

		con=sqlite3.connect('youTube.db')
		c=con.cursor()
		c.execute("""CREATE TABLE youtubers(kyename TEXT,video TEXT, link TEXT);""")		
		Console.log('Enter youtuber key:')
		key=Console.get()

		if key==kalle.keyname:
			kalle.browse()
			kalle.saveInfo()
			c.execute("INSERT INTO youtubers VALUES(?,?,?)",(kalle.keyname,kalle.keyword,kalle.search))
			con.commit()
			con.close()
		elif key==tim.keyname:
			tim.browse()
			tim.saveInfo()
			c.execute("INSERT INTO youtubers VALUES(?,?,?)",(tim.keyname,tim.keyword,tim.search))
			con.commit()
			con.close()
		elif key==kylie.keyname:
			kylie.browse()
			kylie.saveInfo()
			c.execute("INSERT INTO youtubers VALUES(?,?,?)",(kylie.keyname,kylie.keyword,kylie.search))
			con.commit()
		else:
			Console.log('Wrong Key!')
			App()


def insertData():

		con=sqlite3.connect('youTube.db')
		c=con.cursor()	
		Console.log('Enter youtuber key:')
		key=Console.get()

		if key==kalle.keyname:
			kalle.browse()
			kalle.saveInfo()
			c.execute("INSERT INTO youtubers VALUES(?,?,?)",(kalle.keyname,kalle.keyword,kalle.search))
			con.commit()
			con.close()
		elif key==tim.keyname:
			tim.browse()
			tim.saveInfo()
			c.execute("INSERT INTO youtubers VALUES(?,?,?)",(tim.keyname,tim.keyword,tim.search))
			con.commit()
			con.close()
		elif key==kylie.keyname:
			kylie.browse()
			kylie.saveInfo()
			c.execute("INSERT INTO youtubers VALUES(?,?,?)",(kylie.keyname,kylie.keyword,kylie.search))
			con.commit()
		else:
			Console.log('Wrong Key!')
			App()

def App():

	if os.path.isfile('youTube.db'):
		insertData()
	else:
		insertDatawithTable()

App()





