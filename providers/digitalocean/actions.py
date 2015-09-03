#URL: https://api.digitalocean.com/v2/actions

# /Account API Returns:
# id, status, type, started_at, completed_at, resource_id, region, region_slug

#Response Body
# {
#   "actions": [
#     {
#       "id": 36804636,
#       "status": "completed",
#       "type": "create",
#       "started_at": "2014-11-14T16:29:21Z",
#       "completed_at": "2014-11-14T16:30:06Z",
#       "resource_id": 3164444,
#       "resource_type": "droplet",
#       "region": "nyc3",
#       "region_slug": "nyc3"
#     }
#   ],
#   "links": {
#     "pages": {
#       "last": "https://api.digitalocean.com/v2/actions?page=159&per_page=1",
#       "next": "https://api.digitalocean.com/v2/actions?page=2&per_page=1"
#     }
#   },
#   "meta": {
#     "total": 159
#   }
# }

import requests
import json
import arrow
from common import getHeader
from dateutil import tz

__URL = "https://api.digitalocean.com/v2/actions"

#Get list of ALL actions - Completed, in progress 
def getAllActions():
    
    headers = getHeader()
    r = requests.get(__URL, headers=headers)
    
    #Format into an easy-to-read list.
    allactions = json.loads(r.text)
    
    # Returns response in json format.
    return allactions['actions'];


#Print all actions to user's console.
def displayAllActions():
    
    # Get list of actions in json format, store it in a dictionary
    allactions = getAllActions()
    
    #Get the size of allactions dictionary
    numOfActions = len(allactions)

    for index in range(0,numOfActions):
        print "-----------------"
        print "                 "
        print ("Action: " + repr(index + 1) + " - " + allactions[index]['type'] + " " + allactions[index]['resource_type'])
        
        start_time = allactions[index]['started_at']
        completed_time = allactions[index]['completed_at']
        
        # Display 
        start_time = arrow.get(start_time).format('MM-DD-YYYY HH:mm:ss')
        completed_time = arrow.get(completed_time).format('MM-DD-YYYY HH:mm:ss')
        
        print ("Start At: " + repr(start_time))
        print ("Completed At:" + repr(completed_time))
        print "Status: " + allactions[index]['status']
        print "Droplet Location: " + allactions[index]['region_slug']
        
    return;
    


#Display Action by ID

#Display Actions by Status

#Display action by type.

#Display action by date.

#Display action by region
