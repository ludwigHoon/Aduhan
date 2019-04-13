import datetime

# Getting data from facebook chatbot
def getDataFromFacebook(d, lo, la, pd, c, un, cr):
    Date = datetime.datetime.strptime(d, '%d/%m/%Y').date()
    Longitude = lo
    Latitude = la
    ProblemDescription = pd
    Category = c
    Undeserved = un
    Criticality = cr
    row = (Date, Longitude, Latitude, Category, Undeserved, Criticality)
    return(row)
# Getting data from twitter chatbot
def getDataFromTwitter(d, lo, la, pd, c, un, cr):
    return(getDataFromFacebook(d, lo, la, pd, c, un, cr))

# Getting data from form / chatbot
def getDataFromIndependent(d, lo, la, pd, c, un, cr):
    return(getDataFromFacebook(d, lo, la, pd, c, un, cr))

# Processes

