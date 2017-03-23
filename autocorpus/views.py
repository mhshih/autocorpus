from django import forms

class UploadFileForm(forms.Form):
    file=forms.FileField()

def append2DRH(dep,rel,head,DRH):
    if dep not in DRH:DRH[dep]={rel:[head]}
    elif rel not in DRH[dep]:DRH[dep][rel]=[head]
    else:DRH[dep][rel].append(head)

def parse(file):
    chdir('/tmp/stanford-parser-full-2016-10-31')
    system('bash lexparser.sh data/chinese-onesent-utf8.txt > lexparser.parsed')
    DRH=dict() #DRH[dep]={rel:heads}
    for line in open('lexparser.parsed').readlines()[:-1]:
        rel,dep_head=line.split('(')[:2]
        dep,head=[w.split('-')[0] for w in dep_head.split()]
        append2DRH(dep,rel,head,DRH)
    return DRH

from os import chdir,system
from django.http import HttpResponse
def home(request):
    DRH=parse(file='')
    output='<table>'
    for dep,rel_heads in DRH.items():
        output+='<tr><td>%s</td></tr>' % dep
        for rel,heads in rel_heads.items():
            output+='<tr><td></td><td>%s:</td><td>%s</td><tr>' % (rel,' '.join(heads))
    return HttpResponse(output)

