from django.shortcuts import render
from django.http import HttpResponse
#pip install firebase_admin
#real_time Database/ test version 이기 때문에 플러터 개발 어느정도 끝나면 손봐줘야 함.
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import numpy as np

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('ant-indicator-firebase-adminsdk-orxkq-59daefb774.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://ant-indicator-default-rtdb.firebaseio.com/'
})


def index(request):
    dir = db.reference(f'Counting Data/삼성전자/20220124')  #기본 위치 지정
    count = dir.get()
    return render(request, 'indicator/index.html', context=count)

def detail(request):
    return render(request, 'indicator/detail.html')

