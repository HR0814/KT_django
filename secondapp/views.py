from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse('<u>Main</u>')


# import secondapp.models as models
from .models import Course

def insert(request):
    Course(name='데이터 분석',cnt=30).save()
    Course(name='데이터 수집',cnt=20).save()
    Course(name='웹개발',cnt=25).save()
    Course(name='인공지능',cnt=20).save()

    return HttpResponse('데이터 입력 완료')

def show(request):
    course = Course.objects.all()
    result = ''
    for c in course:
        result += '%s %s<br>' % (c.name, c.cnt)

    return HttpResponse(result)