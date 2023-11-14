from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
import os
from django.http import HttpResponse

def index(request):
        if request.method =="POST":
            data = request.POST['link-data']
            img= make(data)
            generated_img= 'qr'+str(time.time())+'.png'
            img.save(os.path.join(settings.MEDIA_ROOT,generated_img))
            return render(request,'index.html',{'generated_img':generated_img})

        return render(request,'index.html')