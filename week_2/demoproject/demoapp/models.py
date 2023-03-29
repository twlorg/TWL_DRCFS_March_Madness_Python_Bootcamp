from django.db import models

class TestDb(models.Model):
    name=models.TextField()
    age=models.IntegerField()

    def __str__(self):
        return self.name 


class NewUser(models.Model):
    firstname=models.TextField()
    lastname=models.TextField()
    email=models.EmailField()

    def __str__(self):
        return self.firstname +' ' + self.lastname
    

class UserMedia(models.Model):
    file=models.FileField()

