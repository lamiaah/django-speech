from  django.urls import path
from chat.Api import views
urlpatterns = [

    path('', views.apirecord),
    
   
]
