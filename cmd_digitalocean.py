#Integrates the custom digitalocean lib into the app.
import lib.digitalocean

#Initialize server.

# Check if filename doesn't already exist.


# Create serverfile.
def cmdCreateDroplet(servername)
    droplet_file = createDroplet(servername)
    
    if (droplet_file != "")
        result = "Succesfully created file at:" droplet_file
        print result
    
    if (droplet_file == "")
        result = "Failed to create file. Already exists?"
        print result
    
    return;
   
    
#Start server

    #Open specified server file.
    def openDroplet(servername)
        
    
    
        return;
    
    
    
    #Load settings from file into variables.
    
    
    #Start the server using values (post)





#Stop server






#Backup Server (Must be enabled on droplet)






#Create snapshot of server (must be powered off first)