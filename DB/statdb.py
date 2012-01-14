from tw import twmessage

from pymongo import Connection

def readdmdata():
    connection = Connection()
    db = connection.test_database
    dms = db.dmlist
    
    msg = dms.find_one()        
    return msg['mid']
    
    

def storedmdata(mid, sid, text):
    connection = Connection()
    db = connection.test_database
    dms = db.dmlist
    dm = {}
    pkey = ""
    pkey += str(mid)
    pkey += str(sid)
    pkey += text
    
    for dm in dms.find({"id": pkey}):        
        #print dm
        return 1

        
    dm = {"id":pkey,
            "mid": mid,
            "sid": sid,
            "text": text 
            }
    dms.insert(dm)
    return 0
    

    
def storeflightdata(querydate, journyedate, tocity, fromcity, flightlist):
    flag = 0
    rflag = 0
    connection = Connection()
    db = connection.test_database
    collection = db.test_collection

    #print db.collection_names()
    #print collection

    for i in xrange(0,len(flightlist), 5):   
        pkey = ""
        pkey+=querydate
        pkey+=journyedate
        pkey+=fromcity
        pkey+=tocity
        
        pkey+=flightlist[i]
        pkey+=flightlist[i+1]
                    
        posts = db.posts
        post = {}
        for post in posts.find({"id": pkey}):
            flag = 1
        
        if (flag == 1):
            flag = 0
            continue
        
            
        post = {"id":pkey,
                "DoJ": journyedate,
                "From": fromcity,
                "To": tocity,
                "Airline":flightlist[i],
                "Time": flightlist[i+1],
                "DoQ" : querydate,
                "fare": flightlist[3],
                "duration" : flightlist[2] 
                }
        posts.insert(post)
        rflag = 1
    return rflag
        
        
    #for post in posts.find():
        #print post

def readflightdata(jdate, fromcity, tocity):
    connection = Connection()
    db = connection.test_database
    collection = db.test_collection

    print db.collection_names()
    print collection
    
    posts = db.posts
    
    for post in posts.find({"DoJ": jdate, "From": fromcity,
                "To": tocity}):
        print post