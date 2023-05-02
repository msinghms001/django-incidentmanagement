from django.urls import path
from .import views

urlpatterns=[
    path('',views.land),
    path('signup/',views.signup),
    path('search/<str:term>',views.search),
    path('view/',views.view),
    path('update/',views.update),
    
]