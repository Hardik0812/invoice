from django.urls import  path
from . import views

urlpatterns = [
    path('client/<str:pk>/name', views.clientName , name="client-name"),
    path('client/<str:pk>/address', views.clientAddress , name="client-address"),
    path('clientname/<str:pk>/address', views.clientnameAddress , name="client-name-address"),
    

]



