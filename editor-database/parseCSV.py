import json
import csv

# Get record
def getCSVRecord(key):
    with open('records.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            if (row[0] == key):
                return row[1]
        return "-1"
    
# Write record
def writeCSVRecord(key, text):
    if (getCSVRecord(key)!="-1"):
        return False
    with open('records.csv', mode='a+',newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([key, text.replace('%20', ' ')])
        return True

# Generate unique id
def genUnique():
    with open('records.csv','rt')as f:
        data = csv.reader(f)
        count = 0
        for row in data:
            count = count + 1
    return count + 1

        # https://www.guru99.com/python-csv.html