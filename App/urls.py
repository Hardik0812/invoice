from django.urls import include, path
from rest_framework import routers
from . import views



# create a router object
router = routers.DefaultRouter()
 
# register the router
router.register(r'clients/<int:pk>/name',views.ClientsViewSet, 'clientname')
router.register(r'clients/<int:pk>/address',views.ClientaddressViewSet, 'clientaddress')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:pk>/name',views.ClientsViewSet)
    
]

