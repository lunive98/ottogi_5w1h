# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from distutils.command.install_egg_info import safe_name
from django.urls import path, re_path
from . import views
from .models import Df1
from .models import Info

urlpatterns = [

    # test
    # path('', views.index)
    path('top/', views.top, name='top'),
    path('traffic/', views.traffic, name='traffic'),
    path('info_data/', views.top, name='info_data'),
    # path('detail/', views.detail, name='detail'),
    #path('search/', views.SearchFormView.as_view(), name='search'),
    # path('town/', views.town)
    #path('top30/', views.top, name='top30'),

    #path('tag/', views.tag, name = 'tag'),
    
    # The home page
    path('', views.index, name='home'),
    # dongghun test
    # path('', views.json_test, name='get_data'),
    # Matches any html file
     # ajax
    path('top5/', views.top5, name='top5'),
    path('tags/', views.tags, name='tags'),
    # 동건 작성중
    # path('info/', views.info_view, name='info_view'),
    path('/recommend/', views.recommend, name='recommend'),
    # path('test_t/', views.test_t),
    path('detail/<int:pid>', views.detail, name='detail'),

    re_path(r'^.*\.*', views.pages, name='pages'),
    # path('top/', views.top_data),


#     path('', views.df1_view, name = 'df1_view'),
]