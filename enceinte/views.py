from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect
from enceinte.models import *
from enceinte.forms import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect,csrf_exempt

import os
import json

# @csrf_protect
@csrf_exempt
def home(request):
    # if (request.is_ajax()):
    print('homepage')
    if request.method == 'POST':
        print('manao ajax')
        hostname = request.POST['name']
        response = os.system("ping -c 1 " + hostname)
        item = Hostname.objects.all()
        json_response = {'hostname' : hostname,'response':response}
        return JsonResponse(json_response)
        # return HttpResponse(json.dumps(json_response), content_type='application/json')
        # return render(request, 'enceinte/index.html', {'hostname': hostname, 'response' : response, 'date': datetime.now(), 'items': item})
    else:
        item = Hostname.objects.all()
        return render(request, 'enceinte/index.html', {'date': datetime.now(), 'items': item})

def dashboard(request):
    # hostname = "google.com"
    # response = os.system("ping -c 1 " + hostname)
    return render(request, 'enceinte/form.html', locals())

@csrf_exempt
def insert(request):
    hostname = Hostname()
    print('insert hostname')
    if request.method=='POST':
        hostname.ip_adress = request.POST['ip_adress']
        print(hostname.ip_adress)
        response = os.system("ping -c 1 " + hostname.ip_adress)
        print(response)
        hostname.save()
        print('hostname saved')
        
    # hostname.ip_adress = "192.168.123.1"
    #hostname.code = 1
    # hostname.save()
    
    # return render(request, 'enceinte/index.html')
    return redirect('/')

def host_get(request):
   hostname = request.GET["name"]
   #and return your results as a HttpResponse object that contains a dict
   #return HttpResponse(json.dumps({'hostname' : hostname}), content_type='application/json')
   #return HttpResponse('OK')
   return render(request, 'enceinte/index.html', {'hostname' : hostname})
   
 def new_user:
    return redirect('/')