from http.client import HTTPResponse
from unittest import result
from django.shortcuts import redirect, render
from django.http import HttpResponse

from secondapp.forms import CourseForm

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

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms.models import model_to_dict
@csrf_exempt
def ajaxGet(request):
    # QuerySet []
    c = Course.objects.all()
    
    data = []
    # model_to_dict - 조회된 데이터를 dict 형태로 변경
    for a in c:
        d = model_to_dict(a)
        data.append(d)
    return JsonResponse(data, safe=False)

def ajaxExam(request):
    
    return render(request, 'secondapp/ajax_exam.html')

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            # 데이터 저장
            course = form.save(commit=False)
            course.save()

            # 어딘가로 이동, 메시지 출력
            return redirect('firstapp:post') 
    else:
        form = CourseForm()


    return render(request, 'secondapp/course_create.html', {'form':form})