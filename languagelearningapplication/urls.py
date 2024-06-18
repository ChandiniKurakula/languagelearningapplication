from django.contrib import admin
from django.urls import path,include
from .views import index
from .views import babbel
from .views import busuu
from .views import duolingo
from .views import memrise
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name= 'index'),
    path('babbel/',babbel,name='babbel'),
    path('busuu/',busuu,name='busuu'),
    path('duolingo/',duolingo,name='duolingo'),
    path('memrise/',memrise,name='memrise'),
    path('accounts/', include('accounts.urls')),
    path('forms/', views.forms, name='forms'),
     path('duolingo/', include('duolingo.urls')),
]