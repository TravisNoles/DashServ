#Module gets/sends/sets common digitalocean api actions.


# Common Headers in every response (example)
# content-type: application/json; charset=utf-8
# status: 200 OK
# ratelimit-limit: 1200
# ratelimit-remaining: 1137
# ratelimit-reset: 1415984218


import yaml
import json
import requests
from os.path import expanduser

#Sets home directory variable when script executes.
__HOME = expanduser("~")

#Full digitalocean api v2 url.
__URL = "https://api.digitalocean.com/v2"

#Function returns the api key for digitalocean.
def getAuthKey():
    #Get settings directory (in user's home)
    configFile = open(__HOME + "/" + "settings.yaml") 
    #Yaml Safeload (doesn't allow for execution in yaml config)
    data = yaml.safe_load(configFile)
    return data["digitalocean"]["authkey"]

#Gets the digitalocean header with authkey
def getHeader():
    #Stores the apikey in local variable, adds the required "Bearer" to header
    API_KEY = "Bearer " + getAuthKey()
    
    #Complete headers.
    headers = {'Content-Type': 'application/json', 'Authorization': API_KEY}

    return headers;
