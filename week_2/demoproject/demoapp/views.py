from django.shortcuts import render
from django.http import HttpResponse
from .models import TestDb


def main(request):
    return HttpResponse("Hello world!")

def another(request):
    return HttpResponse("K xa khabar!!")


def testing_form(request):
    if request.method == "POST":
        testdb=TestDb()
        name=request.POST['your_name']
        age=request.POST['your_age']
        testdb.age=age
        testdb.name=name
        testdb.save()

        print(name, age)
    return render(request, 'testing_form.html')

def good_form(request):
    return render(request, 'goodlookingform.html')