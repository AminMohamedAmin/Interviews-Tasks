from django.conf.urls import url
from django.urls import path

from upload import views
from .views import inlog,saveregisteree,saveinlogee,saveregisterer,saveinloger,ee, saveupdate

urlpatterns = [
    # path('files/',uploadfiles,name='uploadfiles'),
    # url(r'^(?P<id>\d+)/$', read_file, name='read'),
    # path('read/<str:username>/',read_file,name='read'),
    path('',inlog,name='home'),
    path('saveregisteree/',saveregisteree,name='saveregisteree'),
    path('saveinlogee/',saveinlogee,name='saveinlogee'),
    path('saveregisterer/',saveregisterer,name='saveregisterer'),
    path('saveinloger/',saveinloger,name='saveinloger'),
    path('ee/',ee,name='ee'),
    path('saveupdate/', saveupdate, name='saveupdate'),
    # path('er/',er,name='er'),

]