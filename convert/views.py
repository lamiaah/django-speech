from django.shortcuts import render

# Create your views here.
import os
from convert.models import Chat

from django.http import HttpResponse ,Http404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from convert import process

global audio_data
# def index(request):
#     return render(request,'audio.html')



@require_http_methods(['GET', 'POST'])
def record(request):

    # GET method, return HTML page
    if request.method == 'GET':
        samples = Chat.objects.all()
        return render(request, 'audio.html', {'samples': samples})
    # POST request, process the uploaded Audio file
    uploaded_file = request.FILES['uploaded_file'] 
    print(uploaded_file)
    audio_data = Chat.objects.create(uploaded_file=uploaded_file)
    # Begin processing
    process.file(audio_data.id)
    return  redirect('home')


