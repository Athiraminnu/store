from . import views
from django . urls import path

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('btn', views.button, name='button'),
    path('reg-form', views.form, name='form'),
    path('msg', views.msg, name='message'),
    path('logout', views.logout, name='logout')
]
