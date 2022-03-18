from django.db import models
# from __future__ import unicode_literals

class User(models.Model):
    username =   models.CharField(max_length=30)
    password =   models.CharField(max_length=50)
    def __str__(self):
            return self.username
















# class Product(models.Model):
#     name =          models.CharField(max_length=255)
#     description =   models.TextField(null=True,blank=True)
#     price=          models.IntegerField(null=True,blank=True)
#     date_created=   models.DateTimeField(auto_now_add=True, black= True)
#     date_modified=  models.DateTimeField(auto_now=True,blank=True)
#
#     def __unicode__(self):
#         return self.name
#     def to_json(self):
#         return {
#             'id' : self.id,
#             'name' : self.name,
#             'desc' : self.description,
#             'price':self.price,
#             'date_created' : self.date_created,
#             'date_modified' : self.date_modified
#
#         }


# class Celebrity(models.Model):
#     name=models.CharField(max_length=100)
#     worth=models.IntegerField(max_length=20)

# class Customer(models.Model):
#     name=models.CharField(max_length=200)
#     country=models.CharField(max_length=100)


# Create your models here.
