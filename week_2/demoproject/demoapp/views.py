from django.shortcuts import render
from django.http import HttpResponse
from .models import TestDb, NewUser, UserMedia

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

        #print(name, age)
    return render(request, 'testing_form.html')

def good_form(request):
    if request.method == "POST":
        eutainstance=NewUser()
        #eutainstance.firstname=request.POST['first_name']
        #eutainstance.lastname=request.POST['last_name']
        #eutainstance.email=request.POST['email']

        if len(request.POST['first_name'])==0:
            return HttpResponse("Error occured!!")
        if len(request.POST['last_name'])==0:
            return HttpResponse("Error occured!!")
        if len(request.POST['email'])==0:
            return HttpResponse("Error occured!!")
        
        eutainstance.firstname=request.POST['first_name']
        eutainstance.lastname=request.POST['last_name']
        eutainstance.email=request.POST['email']

        eutainstance.save()

    return render(request, 'goodlookingform.html')

def fileupload(request):
    if request.method == "POST":
        backendmedia=UserMedia()
        media=request.POST['files']
        backendmedia.file=media
        backendmedia.save()

    return render(request, 'fileupload.html')


def contextplaying(request):
    users=NewUser()
    print(users.firstname)

    a={"name":"Nabin", "items":['OOP', 'Django', 'networking', 'otherstuffs'], }

    return render(request, 'contextplaying.html', a)


