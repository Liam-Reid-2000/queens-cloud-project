
from datetime import datetime

def writeLog(link, url, status, timeElapsed):
	f = open('logs.txt', 'a')
	f.write(str(datetime.now()) + ' : Attemt to get data from "' + link + '" at URL "' + url + '" Status: ' + str(status) + ' Response time from server: ' + str(timeElapsed))
	f.write('\n')
	f.close()

def writeOverallStatusLog(activeLinks):
	f = open('logs.txt', 'a')
	f.write(str(datetime.now()) + ' : Number of active links at this time: ' + activeLinks)
	f.write('\n')
	f.close()