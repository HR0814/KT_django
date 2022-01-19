from http.client import HTTPResponse
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse('<u>Main</u>')


# import secondapp.models as models
from .models import ArmyShop, Course

def insert(request):
    Course(name='데이터 분석',cnt=30).save()
    Course(name='데이터 수집',cnt=20).save()
    Course(name='웹개발',cnt=25).save()
    Course(name='인공지능',cnt=20).save()

    return HttpResponse('데이터 입력 완료')

def show(request):
    course = Course.objects.all()
    # result = ''
    # for c in course:
    #     result += '%s %s<br>' % (c.name, c.cnt)

    # return HttpResponse(result)

def army_shop(request):
    prd = request.GET.get('prd')
    # prd = request.GET.get('prd', '')

    try:
        shop = ArmyShop.objects.filter(name__contains=prd)
    except:
        shop = ArmyShop.objects.all()

    return render(
        request, 'secondapp/army_shop.html',
        { 'data': shop }
)
def army_shop2(request, year, month):
    shop = ArmyShop.objects.filter(year=year, month=month)
    
    # result = ''
    # for i in shop:
    #     result += '%s %s %s<br>' %(i.year, i.month, i.name)
    # return HTTPResponse(result)

    result = ['%s %s %s<br>' %(i.year, i.month, i.name) for i in shop ]

    return HttpResponse(''.join(result))
