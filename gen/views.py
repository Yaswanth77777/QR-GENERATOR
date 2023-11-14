from django.shortcuts import render
from django.conf import settings
from qrcode import *
from qrcode import make as make_qr_code
import time
import os
from io import BytesIO
import base64
from django.http import HttpResponse

def index(request):
        if request.method =="POST":
            data = request.POST['link-data']
            img = make_qr_code(data)
           # generated_img= 'qr'+str(time.time())+'.png'
           # img.save(os.path.join(settings.MEDIA_ROOT, generated_img))
           # img_url = os.path.join(settings.MEDIA_URL, generated_img)
           # buffer = BytesIO()
           # img.save(buffer, format='PNG')
           # qr_bytes = buffer.getvalue()
           # qr_base64 = base64.b64encode(qr_bytes).decode('utf-8')
            buffered = BytesIO()
            img.save(buffered, format='PNG')
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return render(request,'index.html',{'generated_img':img_str})

        return render(request,'index.html')

