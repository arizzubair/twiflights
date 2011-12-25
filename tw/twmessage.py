#import twitter
from tw import dm
import tweepy 
#import dm
from configobj import ConfigObj

def PostMessage(jdate, fromcity, tocity, message):
    filename = "tw.ini" 
    config = ConfigObj(filename)
    
    consumer_key = config['consumer_key']    
    consumer_secret = config['consumer_secret']
    access_token = config['access_token']
    access_token_secret=config['access_token_secret']
    
    #new comment
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    
    
    data = ""
    data += jdate
    data += " "
    data += fromcity
    data += " "
    data += tocity
    
    i = 1
    for w in message:
        
        if (i % 5 == 3):
            data += ""
        elif (i % 5 == 4):
            data += "Rs. "
            data += w
            data += " "
        elif (i % 5 == 1):
            data += w[:8]
            data += " "
        else:
            data += w
            data += " "
        i += 1
        
    print data
    status = api.update_status(data[:138]+"..")
    print status

        
def read_messages():   
    filename = "tw.ini" 
    config = ConfigObj(filename)
    
    consumer_key = config['consumer_key']    
    consumer_secret = config['consumer_secret']
    access_token = config['access_token']
    access_token_secret=config['access_token_secret']
    
    #new comment
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
    
    print api.me().name
    msgobj_list = []
    msgs =  api.direct_messages()
    for m in msgs:
        newdm = dm.dm(m.text, m.sender_screen_name, m.sender, m.id, m.created_at)
        msgobj_list.append(newdm)
    
    return msgobj_list
        
        
    
    