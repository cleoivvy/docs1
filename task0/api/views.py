from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def Get_info(request):
        email =  "claraojobo@gmail.com",
        current_datetime= datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        github_url= "https://github.com/cleoivvy/docs1.git"
      
        data = {
        'email': email,
        'current_datetime': current_datetime,
        'github_url': github_url
    }
        return JsonResponse(data)
