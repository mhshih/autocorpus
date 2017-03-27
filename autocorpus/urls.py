from django.conf.urls import patterns,url

urlpatterns = patterns('',
    url('query','autocorpus.views.query'),
    url('', 'autocorpus.views.home'),
#   url('upload','autocorpus.views.upload')
)
