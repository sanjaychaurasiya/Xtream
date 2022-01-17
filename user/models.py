from django.db import models


# Create your models here.
class Users(models.Model):
    MUMBAI = 'MUMBAI'
    DELHI = 'DELHI'
    CHENNAI = 'CHENNAI'
    BANGALORE = 'BANGALORE'
    KOLKATA = 'KOLKATA'

    CITY_CHOICES = [
        (MUMBAI, 'Mumbai'),
        (DELHI, 'Delhi'),
        (CHENNAI, 'Chennai'),
        (BANGALORE, 'Bangalore'),
        (KOLKATA, 'Kolkata')
    ]
    email = models.EmailField()
    name_of_receiver = models.CharField(max_length=100)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)

    def __str__(self):
        return self.name_of_receiver
