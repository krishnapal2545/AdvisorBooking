from django.shortcuts import render, redirect
from django.contrib import messages
from User.models import *
import string,random


def index(request):
    if request.session.has_key('userid'):
        Result = {'User':True}
        return render(request,'index.html',Result)
    return render(request,'index.html')


def register(request):
    
    if request.method == 'POST':
        while True :
            userid =''.join(random.choices(string.ascii_uppercase + string.digits,k=6))
            if User.objects.filter(user_id = userid).exists() :
               continue
            else :
                break
        name = request.POST['name']
        email = request.POST['email']
        passw = request.POST['pass']
        cpassw = request.POST['cpass']
        if cpassw != passw :
            mess = "Password and Confirm Password Doesn't match "
            messages.error(request,mess)
            return render(request,'register.html')
        if User.objects.filter(name=name,email=email,password=passw).exists():
            create = User.objects.get(name=name,email=email,password=passw)
            id = create.user_id
            mess = f"Your User ID is {id}"
            messages.success(request,mess)
            return redirect('/login')
        create = User.objects.create(user_id=userid,name=name,email=email,password=passw)
        create.save();
        mess = f"Your User ID is {userid}"
        messages.success(request,mess)
        return redirect('/login')
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        email = request.POST['email']
        passw = request.POST['pass']
        if User.objects.filter(user_id = userid ,email = email , password = passw):
            request.session['userid'] = userid
            return redirect('/')
        else :
            mess = "Login Unsuccesfully"
            messages.error(request,mess)
    return render(request,'login.html')


def logout(request):
    try:
      del request.session['userid']
    except:
      pass
    return redirect("/")

def advisor(request):
    if request.session.has_key('userid'):
        advisor = Advisor.objects.all()
        Result = {'User':True,'Advisors':advisor}
        if request.method == 'POST':
              while True :
                bookid =''.join(random.choices(string.ascii_uppercase + string.digits,k=10))
                if Booking.objects.filter(book_id = bookid).exists() :
                   continue
                else :
                   break
              booktime = request.POST['date']+' '+request.POST['time']
              ad_id = request.POST['ad_id']
              name = request.POST['name']
              photo = request.POST['photo']
              if Booking.objects.filter(user_id=request.session['userid'],book_time=booktime,ad_name= name,ad_pic=photo,ad_id=ad_id).exists():
                mess = "Meeting Book Succesfully"
                messages.success(request,mess)
                return render(request,'advisorlist.html',Result)
              crete = Booking.objects.create(user_id=request.session['userid'],book_id = bookid,book_time=booktime,ad_name= name,ad_pic=photo,ad_id=ad_id)
              crete.save();
              mess = "Meeting Book Succesfully"
              messages.success(request,mess)
        return render(request,'advisorlist.html',Result)
    else:
        return redirect("/")

def booking(request):
    if request.session.has_key('userid'):
        advisor = Booking.objects.filter(user_id=request.session['userid']).all()
        Result = {'User':True,'Advisors':advisor}
        return render(request,'booking.html',Result)
    else:
        return redirect("/")

def admin(request):
    if request.method == 'POST':
        login = request.POST['id']
        passw = request.POST['pass']
        if login == 'Advisor' and passw == 'Django':
            request.session['admin']=True
            return redirect('/add')
        mess = "Login Unsuccesfully"
        messages.success(request,mess)
    return render(request,'adminlogin.html')

def add(request):
    if request.session.has_key('admin'):
      if request.method == 'POST':
          while True :
                ad_id =''.join(random.choices(string.ascii_uppercase + string.digits,k=10))
                if Advisor.objects.filter(ad_id = ad_id).exists() :
                   continue
                else :
                   break
          name = request.POST['name']
          photo = request.POST['photo']
          if Advisor.objects.filter(name=name,photo_url=photo).exists() :
            pass
          else:
              crete =Advisor.objects.create(ad_id=ad_id,name=name,photo_url=photo)
              crete.save();
              mess = "Advisor add Succesfully"
              messages.success(request,mess)
      return render(request,'advisor.html')
    return redirect('/')
