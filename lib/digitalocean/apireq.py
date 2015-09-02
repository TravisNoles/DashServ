#Handles every api request for digitalocean
import requests
import json
import os
import sys
import config

#Get header w/ authentication.
def getHeaderData(service, suburl, params=''):
    API_KEY = getapikey("digitalocean")
    
    #Obtain url
    url = getbaseurl(service, suburl)
    
    #Headers to send with API Key
    headers = {'Content-Type': 'application/json', 'Authorization': API_KEY}
    r = requests.get(url, headers=headers)
    
        return r.headers[params]

def getHeaderStr(suburl)
    headers = {'Content-Type': 'application/json', 'Authorization': API_KEY}
        return headers

def postDataReturnStatusCode(suburl, data):
    
    return status_code
    
    
def postDataReturnData(suburl, payload)
    
    headers = getHeaderStr(suburl)
    r = requests.post(url, json=payload, headers=headers)

    return response_data
    

def deleteDataReturnData(suburl, payload="")
    headers = getHeaderStr(suburl)
    
    return response_data
    
    
