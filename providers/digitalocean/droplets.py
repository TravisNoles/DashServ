import requests
import json
from common import getHeader

# Constant variables
__URL = "https://api.digitalocean.com/v2/droplets"
__DEFAULTVALS = []

#List All Droplets -- send get request to /droplets
def getDroplets():
    
    headers = getHeader()
    r = requests.get(__URL, headers=headers)
    alldroplets = json.loads(r.text)
    
    return alldroplets['droplets'];
    

def displayDroplets():
    
    allDroplets = getDroplets()
    
    #Get number of droplets 
    numOfDroplets = len(allDroplets)
    
    
    for index in range(0, numOfDroplets):
        print "--------------------"
        print "List Droplets"
        print "                 "
        print ("Hostname: " + allDroplets[index]['name'])
        print ("ID: " + repr(allDroplets[index]['id']))
        print ("Memory: " + repr(allDroplets[index]['memory']))
        print ("Virt CPUS: " + repr(allDroplets[index]['vcpus']))
        print ("Disk: " + repr(allDroplets[index]['disk']))
        print ("Locked " + repr(allDroplets[index]['locked']))
        print ("Created At: " + repr(allDroplets[index]['created_at']))
        print ("Status: " + allDroplets[index]['status'])
        print ("Backup IDs: " + repr(allDroplets[index]['backup_ids']))
        print ("Snapshot IDs: " + repr(allDroplets[index]['snapshot_ids']))
        print ("Features: " + repr(allDroplets[index]['features']))
        print ("Region: " + repr(allDroplets[index]['region']))
        print ("Image: " + repr(allDroplets[index]['image']))
        print ("Size: " + repr(allDroplets[index]['size']))
        print ("Size Slug: " + allDroplets[index]['size_slug'])
        print ("Networks: " + repr(allDroplets[index]['networks']))
        print ("Kernel: " + repr(allDroplets[index]['kernel']))
        print ("Next backup: " + repr(allDroplets[index]['next_backup_window']))
        print "--------------------"

    
    
    return;


#Debug:

displayDroplets()




#Can display specific droplet info by id or name.
def displayDropletInfo(id=0, name=""):

    return;


#Create Droplet -- Hostname, 


#Remove Droplet (hostname)




########################################################
# #Create new droplet from file.
# def newDroplet(hostname, region, size, image, ssh_key="", backups=False, ipv6=False, user_data, private_networking=False):

#     #Create a file for reading
#     #Create droplet on digitalocean servers
#     #droplet_settings = {'name': name, "region": region, "size": si ze, "image": image, "ssh_keys": ssh_keys, "backups": backups, "ipv6": ipv6, "user_data": user_data, "private_networking": private_networking}
#     r = requests.post(url, json=payload, headers=headers)
    
#     name = "Test"
#     region = "nyc3"
#     size = "512mb"
#     image = "ubuntu-14-04-x64"
#     ssh_keys = []
#     backups = False
#     ipv6 = False
#     user_data = "null"
#     private_networking = "null"
    
#     # Read status response from headers
    
#     return r.headers['status'];



# # Remove & delete a droplet
# def removedroplet():
#     url = getbaseurl("digitalocean", "droplets")
#     apikey = getapikey("digitalocean")
#     headers = getheader("digitalocean", "droplets", "")
    
#     url = "https://api.digitalocean.com/v2/droplets/6636072"
#     apikey = getapikey("digitalocean")
#     headers = getheader("digitalocean", "droplets", "")
#     r = requests.delete(url, headers=headers)
    
#     return r.status_code;


# #Create droplet

# #Initialize server.

# # Check if filename doesn't already exist.


# # Create serverfile.
# def cmdCreateDroplet(servername)
#     droplet_file = createDroplet(servername)
    
#     if (droplet_file != "")
#         result = "Succesfully created file at:" droplet_file
#         print result
    
#     if (droplet_file == "")
#         result = "Failed to create file. Already exists?"
#         print result
    
#     return;
   
    
# #Start server

#     #Open specified server file.
#     def openDroplet(servername)
        
    
    
#         return;
    
    
    
    #Load settings from file into variables.
    
    
    #Start the server using values (post)





#Stop server






#Backup Server (Must be enabled on droplet)






#Create snapshot of server (must be powered off first)