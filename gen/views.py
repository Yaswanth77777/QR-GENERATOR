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
           buffer = BytesIO()
        img.save(buffer, format='PNG')
        qr_bytes = buffer.getvalue()

       
        qr_base64 = base64.b64encode(qr_bytes).decode('utf-8')
            return render(request,'index.html',{'generated_img':qr_base64})

        return render(request,'index.html')
