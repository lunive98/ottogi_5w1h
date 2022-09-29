# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from asyncio import selector_events
from distutils.log import info
from multiprocessing import connection
from optparse import Values
from unittest import result
import pymysql
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .models import Df1
from .models import Info
from django.core.paginator import Paginator

import pandas as pd
import math
import json
from . import views
import csv
import os
'''
urlpatterns=[
    path('', views.Df1)
]
'''
from .models import Df1, Info
# import get_method


@login_required(login_url="/login/")
def index(request):
    date=request.GET.get('trip-start')
    print('HTML에서 넘어온 date: ', date)
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
    gu_store = request.POST.get('gu')
    print(gu_store)
    number = 3
    try:
        #with connection.cursor() as cursor:
        cursor = connection.cursor()
        top_store = dict()
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
        
        top_store['Top_list'] = top_3
        cursor.close()

        cursor = connection.cursor()
        
        print('first sql end')

        strSql2 = "SELECT DISTINCT Topic1 FROM df1 WHERE 자치구 = '%s'" % (gu_store)

        print(strSql2)

        print('second sql start')
        cursor.execute(strSql2)

        print('second sql end')
        result2 = cursor.fetchall()
        topic = result2
        top_store['Topic'] = topic
        for i in range(7):
            print(top_store['Topic'][i])
        
    except:
        print('failed')
    finally:
        connection.close()
    return JsonResponse(top_store)  


@csrf_exempt
def tags(request):
    test_data = {"test_data": "A"}
    tags = request.POST
    # print(tags)
    print(tags['gu'])
    print(tags)
    where_clause = f"자치구='{tags['gu']}' AND"
    # where_clause = ""
    cnt = 0 
    for key, val in tags.items():
        if cnt == 0 and val != '-':
            where_clause += ' Topic2 = 1 AND'
        elif cnt == 1 and val != '-':
            where_clause += ' Topic3 = 1 AND'
        elif cnt == 2 and val != '-':
            where_clause += ' Topic4 = 1 AND'
        elif cnt < 10:
            if val != '-':
                where_clause += f" Topic1 = '{val}' OR"
        cnt = cnt +1
    print(where_clause)
            
    if where_clause.endswith("AND"):
        print('end with AND')
        where_clause = where_clause[:-3]

    if where_clause.endswith("OR"):
        print('end with OR')
        where_clause = where_clause[:-2]    

    sql = f"select pid from df1 where {where_clause} ORDER BY new_label DESC limit 5 "
    print(sql)
    try:
        cursor = connection.cursor()
        top_store = dict()
        
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

        # 두번째 쿼리
        where_clause_2 = ""
        for pid in result:
            print(pid[0])
            where_clause_2 += f' info.pid = {pid[0]} OR'
        
        if where_clause_2.endswith("OR"):
            print('end with OR')
            where_clause_2 = where_clause_2[:-2]
        
        sql2 = f"SELECT info.pid, info.pname, info.hpSchCateNm, info.mcateNm, info.menu, info.photo, df1.new_label FROM df1 LEFT JOIN info ON info.pid=df1.pid WHERE {where_clause_2} ORDER BY new_label DESC"
        print(sql2)

        cursor.execute(sql2)
        result2 = cursor.fetchall()
        print(result2)

        keys = ['pid','pname','hpSchCateNm','mcateNm', 'menu', 'photo','new_label']
        stores = list()
        for idx, row in enumerate(result2):
            top = dict()
            for idx, data in enumerate(row):
                if keys[idx] == 'new_label':
                    rating = float(data)
                    rating = round(rating,1)
                    top[keys[idx]] = rating
                else:    
                    top[keys[idx]] = data
            stores.append(top)
        
        top_store['stores'] = stores

    except:
        pass
    finally: 
        cursor.close()

    return JsonResponse(top_store)      

#작업중
def tag(request):
    sql = 'select * from info where pid = %s'




def top(request):
    #df1s = Df1.objects.all()
    infos = Info.objects.all()
    paginator = Paginator(infos, 20)
    page_num = request.GET.get('page', '1')
    
    page_obj = paginator.get_page(page_num)
    
    return render(request, 'home/top.html', {'infos' : page_obj})

def traffic(request):
    df1s = Df1.objects.all()
    print(df1s)
    return render(request, 'home/traffic.html', {'df1s' : df1s})

def recommend(request):

    #IBF, CBF
    district = '강남구' 
    pid = 323

    # 폴더
    folder = '../static/assets/filtering_file/'
    # 파일명 생성
    file_IBF = f'IBF_{district}.csv'
    file_CBF = f'CBF_{district}.csv'

    # IBF, CBF 파일 경로
    file_IBF_path = folder + file_IBF
    file_CBF_path = folder + file_CBF

    # IBF, CBF matrix 읽기
    ibf_matrix = pd.read_csv(file_IBF_path, index_col='pid')
    cbf_matrix = pd.read_csv(file_CBF_path, index_col='pid')
    # 열 이름 지정
    ibf_matrix.columns.name = 'pid'
    cbf_matrix.columns.name = 'pid'
    # 자료형 변경
    ibf_matrix.index.astype('int')
    cbf_matrix.index.astype('int')
    ibf_matrix.columns.astype('int')
    cbf_matrix.columns.astype('int')
    # 유사도 높은 가게 추출
    ibf_top_3 = ibf_matrix[pid].sort_values(ascending=False)[:4]
    cbf_top_3 = cbf_matrix[pid].sort_values(ascending=False)[:4]
    # delete self
    # amugunas = pd.read_csv('../static/assets/filtering_file/cbf_강남구')
    # print(amugunas['pid'][0])




    # return render(request, 'home/top.html', {'amugunas': amugunas})
    return render(request, 'home/recommend.html')


# 현희
def detail(request, pid):
    infos = {}
    if request.method == 'GET':
        ######## if not login, redirect login page ########
        if not request.session :
            return redirect('/login/') 
        rr = Info.objects.filter(pid=pid)
        print(f'detail in{pid}')
        infos['pname'] = rr.first().pname
        print(infos['pname'])
        return JsonResponse(infos,status=200)
    print(os.getcwd())
    file = os.getcwd() + '/apps/templates/home/detail.html'
    return render(request, file, {'pid':pid})


# 동건 사진 연동 작성중
# def detail(request): # 읽기
#     print(info)
#     infos = Info.objects.get(pid=323) # Info모든 객체들 불러와서 info변수에 저장
#     return render(request, 'home/detail.html',{'infos' : infos})
    # print(infos)
    # return render(request)
    # context = {
    #     'images':images
    # }  

    # photo
# def shining(request):
#     print('이동건')
#     date=request.GET.get('trip-start')
#     print('HTML에서 넘어온 date: ', date)
#     context = {
#             'date': date,
#         }
#     return render(request, 'home/', context)
# def testtest(request):
#     with open('../static/assets/filtering_file/cbf_강남구.csv', mode='r') as cbf:
#         cbf_reader = csv.reader(cbf)
#         for row in cbf_reader:
#             print(row)
#         print(cbf_reader['pid'][0])  # 필드명을 만들고 싶어서 추가


    # return HttpResponse(status=200)  
# def keyword_up(request,pid):
#     if request.method == 'GET':
#         keyword = keyword.objects.get(id=pid)
#     return render(request, 'recommend.html', {'keyword': keyword})
