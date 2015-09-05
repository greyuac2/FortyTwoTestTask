from django.db import models


class MainPage(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    bdate = models.DateField(blank=False, null=False)
    cemail = models.EmailField(max_length=254)
    cjabber = models.CharField(max_length=100)
    cskype = models.CharField(max_length=100)
    bio = models.TextField()
    ocontacts = models.TextField()

    def __str__(self):
        return self.title
