from django.db import models

# Create your models here.
class UserInformation(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.firstname} {self.lastname}")