
from django.urls import path,include
from . import views
urlpatterns=[
path('index',views.index),
path('register',views.register),
path('registerSave',views.registerSave),
path('login',views.login),
path('loginCheck',views.loginCheck),
path('compose',views.compose),
path('composeSave',views.composeSave),
path('inbox',views.inbox),
path('signout',views.signout),
path('sent',views.sent),
path('changePassword',views.changePassword),
path('changePasswordSave',views.changePasswordSave),
path('checkEmail',views.checkEmail),
]