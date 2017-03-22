from os import chdir,system
from django.http import HttpResponse

def home(request):
    chdir('/tmp/stanford-parser-full-2016-10-31')
    system('bash lexparser.sh data/chinese-onesent-utf8.txt > lexparser.parsed')
    return HttpResponse(201703220528)

