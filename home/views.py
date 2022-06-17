import re
from django.http import HttpResponse
from django.shortcuts import render
from home.models import Contact





# Create your views here.


def home(request):
    # return HttpResponse("this is my home page(/) ")

    context = {'name' : 'rk', 'work':'php'}
    return render(request,'home.html',context)                                                                 


def about(request):
    # return HttpResponse("this is my about page(about) ")
    return render(request,'about.html')


def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        city = request.POST['city']
        email = request.POST['email']
        print(name,city,email)

        ins = Contact(name=name , email=email,city=city)
        ins.save()
        print("the data has been written to the DB")
    # return HttpResponse("this is my contact page(contact) ") 
    return render(request,'contact.html')


    

