import os
import requests
import json
from os.path import expanduser
import yaml

__HOME = expanduser("~")
__SETTINGS_FILE = __HOME + "/" + "settings.yaml"
__BASEURL = "https://api.digitalocean.com/v2/"
__APITOKEN = ""

def getHeaders(data=""):
    headers = ""
    
    #Open and read config file.
    configFile = open(__SETTINGS_FILE)
    
    #Read settings file for api key
    data = yaml.safe_load(configFile)
    
    #Access by key.
    apikey = 'Bearer ' + data['DigitalOcean']['apikey']
    headers = {'Content-Type': 'application/json', 'Authorization': apikey}
    
    #Close the file (to prevent memory leaks obv)
    configFile.close()
    
    return headers;


def getData(suburl):
    apiurl = __BASEURL + suburl

    headers = getHeaders()
    r = requests.get(apiurl, headers=headers)
    data = json.loads(r.text)
    
    return data;
    

def getSizes():
    
    sizesJson = getData('sizes')
    return sizesJson['sizes']
    
    
    
    #List all sizes as slugs string. To call/use: can use for loop
    #sizes = getSizes()
    #print sizes['slugs'][0]
    
    # sizesJson = getJsonData(suburl)
    
    # if (memory==0):
    #     maxSizes = len(sizesJson['sizes'])
        
    #     sizes = {'slugs':[]}
    #     for index in range(0, maxSizes):
    #         sizes['data'].append(sizesJson['sizes'][index]['slug'])
            
    # if (memory==512):
    #     access = 0
        
    # if (memory==1024):
    #     access = 1
        
    # if (memory==2048):
    #     access = 2
        
    # if (memory==4096):
    #     access = 3    
        
    # if (memory==8192):
    #     access = 4
        
    # if (memory==16384):
    #     access = 5
        
    # if (memory==32768):
    #     access = 6    
        
    # if (memory==49152):
    #     access = 7    
        
    # if (memory==65536):
    #     access = 8    
        
#List Droplets
    

#Create Droplets
#def createDroplet(hostname, region, size, image, ssh_keys, backups, ipv6, user_data, private_networking):

def createDroplet():

    name = "example222"
    region = "nyc3"
    size = "512mb"
    image = "ubuntu-14-04-x64" # or int by id (snapshots)
    ssh_keys = []
    backups = "False"
    ipv6 = False
    private_networking = False
    user_data = ""
    
    payload = {'name': name, "region": region, "size": size, "image": image, "ssh_keys": ssh_keys, "backups": backups, "ipv6": ipv6, "user_data": user_data, "private_networking": private_networking}
    
    apiurl = __BASEURL + 'droplets'
    headers = getHeaders()
    r = requests.post(apiurl, json=payload, headers=headers)
    
    #Return created droplet information.
    return r.text
