from django.db import models
import digitalocean

# Create your models here.

class Droplet(models.Model):
    uniqueid = models.CharField(max_length=100)
    hostname = models.CharField(max_length=50)
    ipaddr = models.CharField(max_length=15)
    
    region =
    (
        ('NYC1', 'New York City 1')
        ('NYC2', 'New York City 2')
        ('NYC3', 'New York City 3')
        ('sfo1', 'San Francisco 1')
        ('ams1', 'Amsterdam 1')
        ('ams2', 'Amsterdam 2')
        ('ams3', 'Amsterdam 3')
        ('lon1', 'London 1')
        ('sgp1', 'Singapore 1')
    )
    
    size =
    (
        ('512mb', '512MB')
        ('1gb', '1GB')
        ('2gb', '2GB')
        ('4gb', '4GB')
        ('8gb', '8GB')
        ('16gb', '16GB')
        ('32gb', '32gb')
        ('48gb', '48gb')
        ('64gb', '64gb')
    )
    

    image = models.CharField(max_length=3)
    dateCreated = models.DateTimeField()
    
    
    def __unicode__(self):
        return self.hostname


    def create(cls, hostname):
        Droplet = 
        

class AuthHeader(models.Model):
    






    return self