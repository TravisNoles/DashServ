import apireq

#This file will handle droplets, will be able to create, destroy, list statuses
#of droplets.

# URL_BASE = geturl("droplets")
# URL_DROPLETS = ""
# API_KEY = getapikey("digitalocean")
# HEADERS = getheader("digitalocean", "droplets", "")

#List All Droplets w/ (optional) options. Default values.
def listAllDroplets(hostname="ANY", active=True):
    
    r = requests.get(url, headers=headers)
    r = json.loads(r.text)
    
    
    # http://stackoverflow.com/questions/14547916/how-can-i-loop-over-entries-in-json
    for active_droplets in results['droplets']:
        print 'ID:', active_droplets['id'], '-', 'Hostname:', active_droplets['name']
        
    return;

#Create new droplet from file.
def newDroplet(hostname, region, size, image, ssh_key="", backups=False, ipv6=False, user_data, private_networking=False):

    #Create a file for reading





    #Create droplet on digitalocean servers
    #droplet_settings = {'name': name, "region": region, "size": si ze, "image": image, "ssh_keys": ssh_keys, "backups": backups, "ipv6": ipv6, "user_data": user_data, "private_networking": private_networking}
    r = requests.post(url, json=payload, headers=headers)
    
    name = "Test"
    region = "nyc3"
    size = "512mb"
    image = "ubuntu-14-04-x64"
    ssh_keys = []
    backups = False
    ipv6 = False
    user_data = "null"
    private_networking = "null"
    
    # Read status response from headers
    
    return r.headers['status'];



# Remove & delete a droplet
def removedroplet():
    url = getbaseurl("digitalocean", "droplets")
    apikey = getapikey("digitalocean")
    headers = getheader("digitalocean", "droplets", "")
    
    url = "https://api.digitalocean.com/v2/droplets/6636072"
    apikey = getapikey("digitalocean")
    headers = getheader("digitalocean", "droplets", "")
    r = requests.delete(url, headers=headers)
    
    return r.status_code;


#Create droplet
