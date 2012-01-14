from crawler import yatracrawler
from DB import statdb
from dateutil import *
import time 
import datetime
from tw import twmessage
from tw import dm

import re

def main():
    #last_mid = statdb.readdmdata()
    
    dmlist = twmessage.read_messages()
    
    for dm in dmlist:
        #print dm
        req = dm.text
        dmsid = dm.sender
        dmmid = dm.id
        """
        if (dmmid <= last_mid):
            print "no new msgs anymore!"
            return 0
         """
        if (statdb.storedmdata(dmmid, dmsid, dm.text)):
            #skip: query already answered 
            print "no new msgs anymore!"
            return 0
       
        query = req.split() 
        
        #read jdate, to and from part
        i = 1
        for w in query:
            if i == 1:
                journeydate = w
            if i == 2:
                fromcity = w
            if i == 3:
                tocity = w
            i += 1
        
        if (i != 4):
            print "invalid input "+dm.text
            continue
            
        qdate = datetime.date.today()  
        yr =  qdate.year
        mo =  qdate.month
        da = qdate.day
        
        if re.match("[0-9]", fromcity) or re.match("[0-9]", tocity) or re.match("[A-Za-z]", journeydate):
            print "invalid input "+dm.text
            continue
         
        querydate = ""
        querydate += str(da) + "/" + str(mo) + "/" + str(yr) 
        
        finallist = []
        yatracrawler.getpage(finallist, journeydate, fromcity, tocity)
        
        #print finallist    
        dbret = statdb.storeflightdata(querydate, journeydate, tocity, fromcity, finallist)
        
        if dbret == 1:
            twmessage.PostMessage(journeydate, fromcity, tocity, finallist)
        else:
            print "already published!!"
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()