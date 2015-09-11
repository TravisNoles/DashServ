import os
import requests
import json
from os.path import expanduser
import yaml


__HOME = expanduser("~")
__SETTINGS_FILE = __HOME + "/" + "settings.yaml"
__BASEURL = "https://api.digitalocean.com/v2"

def getHeaders():
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
    
#Get a specific size (based on slug.)
def getSize(slug):
    sizesJson = getData('/sizes')
    
    # Memory Selection
    if (slug=="512mb"):
        access = 0
        
    if (slug=="1gb"):
        access = 1
        
    if (slug=="2gb"):
        access = 2
        
    if (slug=="4gb"):
        access = 3    
        
    if (slug=="8gb"):
        access = 4
        
    if (slug=="16gb"):
        access = 5
        
    if (slug=="32gb"):
        access = 6    
        
    if (slug=="48gb"):
        access = 7    
        
    if (slug=="64gb"):
        access = 8    

    return sizesJson['sizes'][access]
    
    
    #List all sizes as slugs string. To call/use: can use for loop
    #sizes = getSizes()
    #print sizes['slugs'][0]
    
    # sizesJson = getJsonData(suburl)
    
    # if (memory==0):
    #     maxSizes = len(sizesJson['sizes'])
        
    #     sizes = {'slugs':[]}
    #     for index in range(0, maxSizes):
    #         sizes['data'].append(sizesJson['sizes'][index]['slug'])
            

        
#Return droplet information based on droplet number (locally)
#Get droplet by localID (which will be stored in the database
def getAllDroplets():
    data = getData("/droplets")
    return data['droplets']
    
def getNumberOfDroplets():
    data = getData("/droplets")
    return data['meta']['total']

#Get all droplet ids, return list.
def getAllDropletIDs():
    data = getData("/droplets")
    #Get number of droplets.
    numberOfDroplets = getNumberOfDroplets()
    allDropletIDs = []
    
    for index in range(0, numberOfDroplets):
        #cycle through droplets to get IDs.
        allDropletIDs.append(data['droplets'][index]['id'])
    return allDropletIDs
    

def removeDroplet(dropletID):
    data = getData("/droplets")
    
    apiurl = __BASEURL + "/droplets/" + repr(dropletID)
    headers = getHeaders()
    r = requests.delete(apiurl, headers=headers)
    
    
    return r.status_code
    
    
def createDroplet(name, region, size, image, ssh_keys, backups, ipv6, user_data, private_networking):
    #Debug - set droplet info manually.
    #name = "example222"
    #region = "nyc3"
    #size = "512mb"
    # image = "ubuntu-14-04-x64" # or int by id (snapshots)
    # ssh_keys = []
    # backups = "False"
    # ipv6 = False
    # private_networking = False
    # user_data = ""
    
    payload = {'name': name, "region": region, "size": size, "image": image, "ssh_keys": ssh_keys, "backups": backups, "ipv6": ipv6, "user_data": user_data, "private_networking": private_networking}
    
    apiurl = __BASEURL + '/droplets'
    headers = getHeaders()
    r = requests.post(apiurl, json=payload, headers=headers)
    
    #Return created droplet information.
    
    print "Check your email for root password information."
    
    
    return r.text
