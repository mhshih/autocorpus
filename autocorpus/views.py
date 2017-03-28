from django import forms
class UploadFileForm(forms.Form):
    file=forms.FileField()

from parse import read_parse
from django.http import HttpResponse
from django.shortcuts import render
def query(request):
    corpus=request.POST['radio']
    DRH=read_parse(corpus)
    dependent=request.POST['word']
#   return HttpResponse(DRH[dependent].values()[0])
    return render(request,'collocation.htm',{'RH':DRH[dependent]})

def write_RF(RF):
    f=open(RF.name,'wb+')
    for chunk in RF.chunks():f.write(chunk)
    f.close()

from os import listdir
from django.shortcuts import render,redirect
from parse import parse
def home(request):
    corpora=[fn for fn in listdir('.') if fn.endswith('out')]
    if request.method=='GET':
        return render(request,'template.htm',{'corpora':corpora,'upload_form':UploadFileForm()})
    elif request.method=='POST':
        RF=request.FILES['file']
        write_RF(RF)
        parse(filename=RF.name)
        return redirect('/')

