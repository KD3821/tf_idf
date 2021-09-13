from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
# from .models import UserFile

from .utils import save_file



def get_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            save_file(request.FILES['file'])
            return HttpResponse("Working!")
        else:
            return HttpResponse("No file!")
    else:
        form = UploadFileForm()
    return render(request, 'form_upload.html', {'form': form})

