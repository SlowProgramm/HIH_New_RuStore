from django.contrib import admin
from django.urls import path, URLPattern
from main.views import *

urlpatterns: list[URLPattern]  = [
    path('', index_view, name='home'),
    path('about/', about_view, name='about'),
    path('create/', create_view, name='create'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),
]
