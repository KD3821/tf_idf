from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Dict, Word, TempD, Idf

from .utils import save_file, read_file
import math



def get_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            save_file(request.FILES['file'])
            read_file(request.FILES['file'])
            return render(request, 'form_upload2.html', {'form': form})
        else:
            return HttpResponse("No file!")
    else:
        form = UploadFileForm()
    return render(request, 'form_upload.html', {'form': form})


def get_idf(request):
    idf_tmp = Idf.objects.all()
    idf_tmp.delete()
    idf_lst = []
    idf_d = {}
    idf_final = {}
    qs = Dict.objects.all().filter()
    tmp = TempD.objects.all().filter()

    for p in qs:
        lst = p.doc_dict
        for s in tmp:
            t_lst = s.temp_dict
            for key in t_lst.keys():
                if key in lst:
                    idf_lst.append(key)
                else:
                    pass
    for s in tmp:
        t_lst = s.temp_dict
        for key in t_lst.keys():
            value = idf_lst.count(key)
            idf_d.setdefault(key, value)

    for key,value in idf_d.items():
        a = len(qs)/value
        res = round(math.log(a), 3)
        idf_final.setdefault(key, res)

    k = Idf(idf_dict=idf_final)
    k.save()

    for s in tmp:
        h = s.temp_dict

    total_w = len(h)
    for key, value in h.items():
        w = Word(word_text=key, tf_amount=round((value/total_w), 3), idf_amount=idf_final.get(key))
        w.save()


    words_list = Word.objects.all().order_by('-idf_amount')[:50]
    context = {'words_list': words_list}
    return render(request, 's_content.html', context)


def get_new(request):
    qs = Dict.objects.all().filter()
    tmp = TempD.objects.all().filter()
    idf = Idf.objects.all().filter()
    d = Word.objects.all().filter()
    qs.delete()
    tmp.delete()
    idf.delete()
    d.delete()

    form = UploadFileForm()
    return render(request, 'form_upload.html', {'form': form})