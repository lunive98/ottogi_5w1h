# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from multiprocessing import connection
from optparse import Values
from unittest import result
import pymysql
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .models import Df1
from .models import Info

import math
import json
from . import views
'''
urlpatterns=[
    path('', views.Df1)
]
'''
from .models import Df1, Info
# import get_method


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    # except:
    #     html_template = loader.get_template('home/page-500.html')
    #     return HttpResponse(html_template.render(context, request))

# @csrf_exempt
# def top5(request):
#     gu_store = request.POST.get('gu')
    
#     number = 3
#     send_message = {'gu':'number'}
#     print(gu_store)
#     try:
#         cursor = connection.cursor()

#         strSql = "SELECT info.pid, info.pname, info.photo, df1.new_label FROM df1 LEFT JOIN info ON info.pid=df1.pid WHERE info.district = %s ORDER BY new_label DESC limit %s"
#         cursor.execute(strSql, (gu_store, number))
#         result = cursor.fetchall()
#         # connection.commit()
#         keys = ['pid','pname','photo','new_label']
#         a=[]
#         dictionary=[]
#         for i in range(3): # 가게 5개
#             # for j in range(1): # 
#                 a = {string: result[i][j] for j , string in enumerate(keys)}
#                 dictionary.append(a) 
#                 print(dictionary)
#                 # [{d:a},{1:3}]
#     except:
#         print('failed')
#     finally:
#         connection.close()
#     return JsonResponse(send_message)  

@csrf_exempt
def top5(request):
    print('test_t 실행')
    gu_store = request.POST.get('gu')
    send_message = {'gu':gu_store}
    print(gu_store)
    number = 3
    try:
        cursor = connection.cursor()
        # hpSchCateNm, mcateNm, menu
        strSql = "SELECT info.pid, info.pname, info.hpSchCateNm, info.mcateNm, info.menu, info.photo, df1.new_label FROM df1 LEFT JOIN info ON info.pid=df1.pid WHERE info.district = %s ORDER BY new_label DESC limit %s"
        cursor.execute(strSql, (gu_store, number))
        result = cursor.fetchall()
        # connection.commit()
        keys = ['pid','pname','hpSchCateNm','mcateNm', 'menu', 'photo','new_label']
        top_3 = list()
        for idx, row in enumerate(result):
            top = dict()
            for idx, data in enumerate(row):
                if keys[idx] == 'new_label':
                    rating = float(data)
                    print(rating)
                    rating = round(rating,1)
                    print(rating)
                    top[keys[idx]] = rating
                else:    
                    top[keys[idx]] = data
            top_3.append(top)
        top_store = dict()
        top_store['Top_list'] = top_3
        
    except:
        print('failed')
    finally:
        connection.close()
    return JsonResponse(top_store)  



def top_data(request):
    try:
        cursor = connection.cursor
        query = 'select * from info left outer join df1 on info.pid = df1.pid limit 30;'
        result = cursor.execute(query)
        tops = cursor.fetchall()

        connection.commit()
        connection.close()

    except:
        connection.rollback()
        print("ERROR")

    context = {'tops' : tops}

    return render(request, 'home/top.html', context)


def top(request):
    df1s = Df1.objects.all()
    infos = Info.objects.all()
    print(df1s)
    return render(request, 'home/top.html', {'df1s' : df1s, 'infos' : infos})

def traffic(request):
    df1s = Df1.objects.all()
    print(df1s)
    return render(request, 'home/traffic.html', {'df1s' : df1s})

"""

# 동건 사진 연동 작성중
def info_view(request): # 읽기
    print('test')
    infos = Info.objects.get(pid=323) # Info모든 객체들 불러와서 info변수에 저장
    # return render(request, 'index.html',{'infos':infos})
    print(infos)
    return render(request)
    # context = {
    #     'images':images
    # }  

    # photo """

    ###########2022_0928_15:10:00
    # -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from multiprocessing import connection
from optparse import Values
from unittest import result
import pymysql
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .models import Df1
from .models import Info

import math
import json
from . import views
'''
urlpatterns=[
    path('', views.Df1)
]
'''
from .models import Df1, Info
# import get_method


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    # except:
    #     html_template = loader.get_template('home/page-500.html')
    #     return HttpResponse(html_template.render(context, request))

# @csrf_exempt
# def top5(request):
#     gu_store = request.POST.get('gu')
    
#     number = 3
#     send_message = {'gu':'number'}
#     print(gu_store)
#     try:
#         cursor = connection.cursor()

#         strSql = "SELECT info.pid, info.pname, info.photo, df1.new_label FROM df1 LEFT JOIN info ON info.pid=df1.pid WHERE info.district = %s ORDER BY new_label DESC limit %s"
#         cursor.execute(strSql, (gu_store, number))
#         result = cursor.fetchall()
#         # connection.commit()
#         keys = ['pid','pname','photo','new_label']
#         a=[]
#         dictionary=[]
#         for i in range(3): # 가게 5개
#             # for j in range(1): # 
#                 a = {string: result[i][j] for j , string in enumerate(keys)}
#                 dictionary.append(a) 
#                 print(dictionary)
#                 # [{d:a},{1:3}]
#     except:
#         print('failed')
#     finally:
#         connection.close()
#     return JsonResponse(send_message)  

@csrf_exempt
def top5(request):
    print('test_t 실행')
    gu_store = request.POST.get('gu')
    send_message = {'gu':gu_store}
    print(gu_store)
    number = 3
    try:
        cursor = connection.cursor()
        # hpSchCateNm, mcateNm, menu
        strSql = "SELECT info.pid, info.pname, info.hpSchCateNm, info.mcateNm, info.menu, info.photo, df1.new_label FROM df1 LEFT JOIN info ON info.pid=df1.pid WHERE info.district = %s ORDER BY new_label DESC limit %s"
        cursor.execute(strSql, (gu_store, number))
        result = cursor.fetchall()
        # connection.commit()
        keys = ['pid','pname','hpSchCateNm','mcateNm', 'menu', 'photo','new_label']
        top_3 = list()
        for idx, row in enumerate(result):
            top = dict()
            for idx, data in enumerate(row):
                if keys[idx] == 'new_label':
                    rating = float(data)
                    rating = round(rating,1)
                    top[keys[idx]] = rating
                else:    
                    top[keys[idx]] = data
            top_3.append(top)
        top_store = dict()
        top_store['Top_list'] = top_3
        
    except:
        print('failed')
    finally:
        connection.close()
    return JsonResponse(top_store)  



def top_data(request):
    try:
        cursor = connection.cursor
        query = 'select * from info left outer join df1 on info.pid = df1.pid limit 30;'
        result = cursor.execute(query)
        tops = cursor.fetchall()

        connection.commit()
        connection.close()

    except:
        connection.rollback()
        print("ERROR")

    context = {'tops' : tops}

    return render(request, 'home/top.html', context)


def top(request):
    df1s = Df1.objects.all()
    infos = Info.objects.all()
    print(df1s)
    return render(request, 'home/top.html', {'df1s' : df1s, 'infos' : infos})

def traffic(request):
    df1s = Df1.objects.all()
    print(df1s)
    return render(request, 'home/traffic.html', {'df1s' : df1s})

"""

# 동건 사진 연동 작성중
def info_view(request): # 읽기
    print('test')
    infos = Info.objects.get(pid=323) # Info모든 객체들 불러와서 info변수에 저장
    # return render(request, 'index.html',{'infos':infos})
    print(infos)
    return render(request)
    # context = {
    #     'images':images
    # }  

    # photo """