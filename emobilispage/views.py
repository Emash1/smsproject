from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .models import Emobilispage
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

@csrf_exempt
def addstudent(request):
    if request.method == 'POST':
        studfname=request.POST.get('studfname')
        studlname=request.POST.get('studlname')
        studemail=request.POST.get('studemail')
        studcourse=request.POST.get('studcourse')

        obj1=Emobilispage(studfname=studfname,studlname= studlname,studemail=studemail,studcourse=studcourse)
        obj1.save()

    #fetch the student data to be displayed
    data = Emobilispage.objects.all();
    context = {'data':data}
    return render(request, 'register.html', context)

