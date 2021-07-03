from django.contrib import admin
from .models import *

class Useradmin(admin.ModelAdmin):
    list_display=[ 'id','user_id','name','email','password']

class Bookadmin(admin.ModelAdmin):
    list_display = ['id','user_id','ad_name','ad_id','book_id','book_time']


class Advisoradmin(admin.ModelAdmin):
    list_display=['id','ad_id','name']


admin.site.register(Advisor,Advisoradmin)
admin.site.register(User,Useradmin)
admin.site.register(Booking,Bookadmin)
