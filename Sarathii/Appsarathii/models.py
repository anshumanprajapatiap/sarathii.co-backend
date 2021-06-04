from django.db import models

# Create your models here.
class Registration(models.Model):
    Email = models.TextField(null=True)
    Name = models.TextField(null=True)
    About = models.TextField(null=True)
    Type = models.TextField(null=True)
    Worth = models.TextField(null=True)
    Condition = models.TextField(null=True)
    Team = models.TextField(null=True)
    Hereaboutsarathii = models.TextField(null=True)
    Helpyou = models.TextField(null=True)
    Yourrecentcustomers = models.TextField(null=True)
    Address = models.TextField(null=True)
    Streetnumber = models.TextField(null=True)
    Zipcode = models.TextField(null=True)
    Service = models.TextField(null=True)
    YourName = models.TextField(null=True)
    Phone = models.TextField(null=True)
    other = models.TextField(null=True)

    def __str__(self):
        return self.Email + '--' + self.Name


class Contact(models.Model):
    Email = models.EmailField(null=True)
    Phone = models.IntegerField(null=True)
    Topic = models.TextField(null=True)
    Yourmessage = models.TextField(null=True)

    def __str__(self):
        return self.Email


class Newsletter(models.Model):
    Email = models.EmailField(null=True)

    def __str__(self):
        return self.Email