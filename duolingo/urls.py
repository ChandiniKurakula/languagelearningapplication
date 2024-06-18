from django.urls import path 

from .  import views

urlpatterns = [
    path('create/', views.Duolingo_create, name='Duolingo_create'),
    # path('<int:pk>/update/', views.Duolingo_update, name='Duolingo_update'),
    # path('<int:pk>/delete/', views.Duolingo_delete, name='Duolingo_delete'),
     
]