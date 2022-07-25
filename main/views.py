from django.shortcuts import render
from main.models import *

def index(request):

    curs = Courses.objects.all()
    new = New.objects.order_by('-id')[:1]
    new_1 = New.objects.order_by(('id'))[:3]
    techer = Teacher.objects.order_by('-id')[:4]

    ctx = {
        "curs": curs,
        'new': new,
        "new_1": new_1,
        'techer': techer

    }
    return render(request, 'main/index.html', ctx)


def course(request):
    course = Courses.objects.all()

    ctx = {
        'course': course
    }

    return render(request, 'main/courses.html', ctx)




def teacher(request):
    teacher = Teacher.objects.all()

    ctx = {
        'teacher': teacher
    }

    return render(request, 'main/teachers.html', ctx)



def new(request):
    new = New.objects.all()
    course = Courses.objects.all()
    teacher = Teacher.objects.all()
    ctx = {
        "new": new,
        'course': course,
        "teacher": teacher
    }


    return render(request, 'main/blog.html', ctx)




def contact(request):


    return render(request, 'main/contact.html')



