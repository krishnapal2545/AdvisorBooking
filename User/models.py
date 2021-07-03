from django.db import models
from django.db.models.fields import CharField, EmailField

class User(models.Model):
    user_id = CharField(max_length=10)
    name = CharField(max_length=10)
    email = EmailField()
    password =CharField(max_length=10)

class Booking(models.Model):
    user_id = CharField(max_length=10)
    book_id = CharField(max_length=100)
    book_time = CharField(max_length=100)
    ad_name = CharField(max_length=100)
    ad_pic = CharField(max_length=2083)
    ad_id = CharField(max_length=100)

class Advisor(models.Model):
    ad_id = CharField(max_length=100,default=None)
    name = CharField(max_length=200)
    photo_url= CharField(max_length=2083)
