"""DashServ - ALPHA Testing

Usage:
    dashserv server init <hostname> <provider>
    dashserv server start <hostname>
    dashserv server stop <hostname>
    dashserv server destroy <hostname>
    dashserv server snapshot <hostname>
    dashserv server ssh <hostname>
    dashserv status <ratelimits>
    dashserv todo <hostname> <task>
    dashserv authorize <provider>
    
Options:
    --version
    --help
    
Examples:
    dashserv server init digitalocean
    
"""

from docopt import docopt
import lib.digitalocean

if __name__ == '__main__':
    arguments = docopt(__doc__, version='DashServ 0.1.0')
    print(arguments)
    
#Init (create config file) Digital Ocean Server
if arguments['server'] == True and arguments['init'] == True and arguments['<provider>'] == 'digitalocean':
    serverfilename = createserverfile(arguments['<server_name>'], arguments['<provider>'])

##Parse the specified server (file) and upload the parsed information to digital ocean   
if arguments['server'] == True and arguments['init'] == True and arguments['<provider>'] == 'digitalocean':
    serverfilename = createserverfile(arguments['<server_name>'], arguments['<provider>'])
