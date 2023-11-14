from django.shortcuts import render
from django.conf import settings
from qrcode import make as make_qr_code
import os
import io
import base64
from django.http import HttpResponse

def index(request):
        if request.method =="POST":
            data = request.POST['link-data']
            img = make_qr_code(data)
            buffer = io.BytesIO()
            img_save.save(buffer, format="PNG")
            img_str = base64.b64encode(buffer.getvalue()).decode()
            return render(request,'index.html',{'generated_img':img_str})

        return render(request,'index.html')

