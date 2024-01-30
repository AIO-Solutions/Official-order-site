from django.shortcuts import render
from .models import About
from django.http import FileResponse,HttpResponse
import os
from django.conf import settings
def team(request):
    form=About.objects.all()
    return render(request,"team.html",{"form":form})


def serve_media(request, file_path):
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)

    # Check if the file exists
    if os.path.exists(file_path):
        # Serve the file using FileResponse
        response = FileResponse(open(file_path, 'rb'))
        return response
    else:
        HttpResponse("Not Found")