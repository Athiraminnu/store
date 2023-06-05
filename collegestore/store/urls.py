from . import views
from django . urls import path

urlpatterns = [
    path('', views.clghome, name='clg_homePg'),
]
