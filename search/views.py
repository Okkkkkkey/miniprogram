from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import json
# Create your views here.
import requests


def search(request):
    data = json.loads(request.body.decode())
    kw = data['kw']
    del data['kw']

    search_api = "http://music.163.com/api/search/pc?s=" + kw
    rsp = requests.post(url=search_api,data=data)

    return HttpResponse(rsp.text)
