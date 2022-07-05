from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Allcourses, details

def Courses(request):
    ac = Allcourses.objects.all()
    template = loader.get_template('TechCourses/courses.html') #a new dir and html page is creted for home page
    context ={
        'ac': ac,
    }                                #context is a dictionary mapping template variable name to python objects
    return HttpResponse(template.render(context, request))       #for homepage>. add in url in urls.py

def detail(request, course_id):                       #to create detail page >> add url in urls.py
    try:
        course = Allcourses.objects.get(pk=course_id)
    except Allcourses.DoesNotExist:
        raise Http404("Course Not Available. Try in available courses")

    return render(request, 'TechCourses/details.html', {'course': course})