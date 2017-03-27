from django import forms
class UploadFileForm(forms.Form):
    file=forms.FileField()

def append2DRH(dep,rel,head,DRH):
    if dep not in DRH:DRH[dep]={rel:[head]}
    elif rel not in DRH[dep]:DRH[dep][rel]=[head]
    else:DRH[dep][rel].append(head)

from subprocess import call
from os import chdir,system,listdir
def parse(filename='chinese-onesent-utf8.txt'):
    DRH=dict() #DRH[dep]={rel:heads}
    command='cd /home/simon/stanford-parser-full-2016-10-31; java -mx150m -cp "*:" edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "typedDependencies" edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz data/english-onesent.txt > /tmp/autocorpus/english-onesent.txt.out'
    print(command)
    system(command)
    for line in open('/tmp/autocorpus/english-onesent.txt.out').readlines()[:-1]:
        rel,dep_head=line.split('(')[:2]
        dep,head=[w.split('-')[0] for w in dep_head.split()]
        append2DRH(dep,rel,head,DRH)
    return DRH

from django.http import HttpResponse
def query(request):
    corpus=request.POST['radio']
    return HttpResponse(corpus)

from django.shortcuts import render,redirect
def home(request):
    corpora=[fn for fn in listdir('.') if fn.endswith('out')]
    if request.method=='GET':
        return render(request,'template.htm',{'corpora':corpora,'upload_form':UploadFileForm()})
    elif request.method=='POST':
#       f=request.FILES['file']
#       t=open(f.name,'wb+')
#       for chunk in f.chunks():t.write(chunk)
        return redirect('/')
        return HttpResponse('<input type=radio name=radio value=%s />%s' % (corpora[0],corpora[0]))

        output='<table>'
        DRH=parse()#filename=f.name)
        for dep,rel_heads in DRH.items():
            output+='<tr><td>%s</td></tr>' % dep
            for rel,heads in rel_heads.items():
                output+='<tr><td></td><td>%s:</td><td>%s</td><tr>' % (rel,' '.join(heads))
        return HttpResponse(output)
