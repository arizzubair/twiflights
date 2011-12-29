from crawler import yatracrawler
from DB import statdb
from dateutil import *
import time 
import datetime
from tw import twmessage
from tw import dm

def main():
    dmlist = twmessage.read_messages()
    
    dm = dmlist[0]
    #print dm
    req = dm.text
    dmid = dm.sender
    
        
    query = req.split() 
    
    i = 1
    for w in query:
        if i == 1:
            journeydate = w
        if i == 2:
            fromcity = w
        if i == 3:
            tocity = w
        i += 1
    
    qdate = datetime.date.today()  
    yr =  qdate.year
    mo =  qdate.month
    da = qdate.day

     
    querydate = ""
    querydate += str(da) + "/" + str(mo) + "/" + str(yr) 
    
    finallist = []
    yatracrawler.getpage(finallist, journeydate, fromcity, tocity)
    
    #print finallist    
    statdb.storeflightdata(querydate, journeydate, tocity, fromcity, finallist)
    
    twmessage.PostMessage(journeydate, fromcity, tocity, finallist)
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()