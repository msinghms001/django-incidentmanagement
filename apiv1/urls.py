from django.urls import path
from .import views

urlpatterns=[
    path('',views.land),
    path('register/',views.signup),
    path('login/',views.login),
    path('search/<str:term>',views.search),
    path('create/',views.create),
    path('view/',views.view),
    path('update/',views.update),
    
]