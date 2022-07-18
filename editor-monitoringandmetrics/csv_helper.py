import csv
from datetime import datetime, timedelta
from logsHelper import writeLog

def writeToStatusCSV(link, url, error, timeElapsed):
    datetimeNow = datetime.now()
    statusFile = open('status.csv','a',newline='')
    writer = csv.writer(statusFile)
    if (error == True):
        writer.writerow([datetimeNow, link, url, "live",timeElapsed])
        writeLog(link, url, "live",timeElapsed)
    else:
        writer.writerow([datetimeNow, link, url, "down",timeElapsed])
        writeLog(link, url, "down",timeElapsed)
    statusFile.close()

def writeToOverallStatusCSV(noLiveLinks):
    datetimeNow = datetime.now()
    statusFile = open('overAllStatus.csv','a',newline='')
    writer = csv.writer(statusFile)
    writer.writerow([datetimeNow, noLiveLinks])


# Calculate uptime for last hour
def get_uptime_last_hour(link):
    
    # Read data from csv
    file = open ('status.csv')
    csvreader = csv.reader(file)
    last_hour_date_time = datetime.now() - timedelta(hours = 1)
    
    # Counts to calcualte metric later
    liveCount = 0
    downCount = 0

    # Get number of live and down links from rows
    for row in csvreader:
        datetime_then = row[0]
        if ((row[1] == link) and (datetime.strptime(datetime_then, "%Y-%m-%d %H:%M:%S.%f") > last_hour_date_time)):
            if (row[3] == 'live'):
                liveCount = liveCount + 1
            else:
                downCount = downCount + 1
    file.close()

    # Calculate uptime if has live links in csv
    if (liveCount > 0):
        uptime = liveCount/(liveCount + downCount) * 100
        return ("%.1f" % uptime) 
    return '0'


# Get average response time for last hour
def get_average_response_time_last_hour(link):
    
    # read csv
    file = open ('status.csv')
    csvreader = csv.reader(file)

    # calculate last hour
    last_hour_date_time = datetime.now() - timedelta(hours = 1)
    
    # Variables to calcualte metric later
    responseTimeTotal = 0
    noResponses = 0
    
    # Get only rows for last hour
    # Get only responsive times for specific link
    for row in csvreader:
        datetime_then = row[0]
        if ((row[1] == link) and (datetime.strptime(datetime_then, "%Y-%m-%d %H:%M:%S.%f") > last_hour_date_time)):
            responseTimeTotal = responseTimeTotal + float(row[4])
            noResponses = noResponses + 1
    file.close()

    # Calculate average response time
    if (noResponses > 0):
        averageResponseTime = responseTimeTotal/noResponses
        return ("%.1f" % averageResponseTime) 
    return 'N/A'
    