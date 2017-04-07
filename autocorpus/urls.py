from django.conf.urls import patterns,url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url('query','autocorpus.views.query'),
    url('^$', 'autocorpus.views.home'),
#   url('upload','autocorpus.views.upload')
)  +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
