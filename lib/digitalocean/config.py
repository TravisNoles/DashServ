import os
import sys
import json
import getpass
import ConfigParser
import config


#Configure Paths
__BASE_DIR = os.path.dirname(os.getcwd())
__RUN_PATH = os.path.abspath(sys.argv[0]) 
__CONFIG_PATH = __BASE_DIR + "config/config.json"
__SERVERS_PATH = __BASE_DIR + "servers" 
__USERNAME = getpass.getuser()

#Set Default Values
__DigitalOceanDefaultVals = []




#Return Paths
def getBasePath():
    return __BASE_DIR
    
def getUsernameSys():
    return __USERNAME
    
def getConfigPath():
    return __PATH_CONFIG
    
def getRunPath()
    return __RUN_PATH

def getAPIURL(provider, suburl="")
    with open(CONFIG_PATH) as data_file:


    return apiurl




#Get API URL Dynamically, request object is optional.
def getUrl(provider, suburl="", reqobj=""):
    
    #Open CONFIG_FILE
    
    
    with open(CONFIG_PATH) as data_file:
        data = json.load(data_file)

    #Combine URL into the requesting url then return it.
    url = DIGITALOCEAN_BASE_API + "/" + suburl
    
    return url;


def parseDroplet(file)

    config = ConfigParser()
    CONFIG_FILE = getConfigPath()
    config.read(file)
    hostname = config.get('
    
    return file;
    
    
    
TEMPLATE = """ #DigitalOcean Example Template
#Settings marked with "NotImplemented" are...not implemented yet

[VirtMachine]
hostname = {servername}
provider = {provider}






[MachineSettings]

#Set active to true if you want it on digitalocean servers. 
active: False

#Hostname - Name of server and physical hostname
Hostname: {servername}
Provider: {provider}
Size: 5

#ubuntu-14-04-x64
distro: ubuntu
version 14.04
arch: x64
    
    
[SSHSettings]
SSHUsername: NotImplemented
SSHPassword: NotImplemented
    
#SSH key to login with
DigitalOceanSSHKey: NotImplemented
    
[DataSettings]
    
#Always scrub the data after destroying this droplet.
always_scrub: NotImplemented
    
    
[Snapshots]
    
#Default Name of snapshot
snapshot_name: digitalocean_example
    
#Automatically create snapshot after shutting down server.
snapshot_always: True
    
    
[Backups]
    
#Automatically create backups
    
BackupFrequency: NotImplemented 
BackupTime = NotImplemented
LocalBackups = NotImplemented
DigitalOceanBackups = NotImplemented
BackupSettings = NotImplemented
    
[OptionalSettings]
backups: True
user_data: null
    
    
#WARNING: Do not remove/alter the below values. It will have unintended consequences.
[ProviderValues]"""


#Create a server file template (init)
def createDroplet(servername):

    filename = SERVER_CONFIG_BASE + servername


    context = {
        "servername":servername,
        "provider":provider
    }    
    
    with open(filename, 'w') as myfile:
        myfile.write(template.format(**context))
    
    
    print "Created server file in servers directory."
    
    
    return filename


createDroplet("TEST.INI")