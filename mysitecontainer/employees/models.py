from django.db import models


class employees(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15) # validators should be a list
    group = models.CharField(max_length=20)
    def __str__(self):
        return self.phone_number#u'%s %s' % (self.fname, self.lname, self.phone_number)
        
		
class empgroups(models.Model):
    title = models.CharField(max_length=8)
    members = models.ManyToManyField(employees)
    def __str__(self):
        return self.title