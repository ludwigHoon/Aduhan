import datetime
import csv

# Getting data from facebook chatbot
def getDataFromFacebook(d, lo, la, pd, c, un, cr):
    Date = datetime.datetime.strptime(d, '%d/%m/%Y').date()
    Longitude = lo
    Latitude = la
    ProblemDescription = pd
    Category = c
    Undeserved = un
    Criticality = cr
    row = [Date, Longitude, Latitude, Category, Undeserved, Criticality]
    return(row)
# Getting data from twitter chatbot
def getDataFromTwitter(d, lo, la, pd, c, un, cr):
    return(getDataFromFacebook(d, lo, la, pd, c, un, cr))

# Getting data from form / chatbot
def getDataFromIndependent(d, lo, la, pd, c, un, cr):
    return(getDataFromFacebook(d, lo, la, pd, c, un, cr))

def checkLocationModel(long, la):
    # Check if location within range of model
    result = True
    return(result)

def checkTextModel(text):
    text = text.strip()
    text = text.split(" ")
    import csv

    with open("flagged.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(dict(row))
    csvFile.close()

    # Use the dict to calculate True/False, confidence
    result = True
    conf = 0.95
    return(result, conf) 

# Processes
def ProcessData(data):
    if data[5] == "1":
        # Check model anyhow 
        # If confidence level low --> verify by users
        # Save content for future training
        pass
    elif checkLocationModel(data[1], data[2]):
        data[5] = "1"
    else:
        un, conf = checkTextModel(data[5])
        if ((un == True) and (conf < 0.85)):
            # Hold --> verify by users
            pass
        elif (un):
            data[5] = "1"
    csv.register_dialect('myDialect',
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True)
    data = [data]
    with open("sampleData.csv", "a") as file:
        writer = csv.writer(file, dialect='myDialect')
        writer.writerows(data)
    file.close()
