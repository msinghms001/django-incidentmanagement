from django.urls import path
from .import views

urlpatterns=[
    path('',views.land),
    path('register_user/',views.signup),
    path('login_user/',views.login),
    path('search_incident/<str:term>',views.search),
    path('create_incident/',views.create),
    path('view_incident/',views.view),
    path('update_incident/',views.update),
    
]