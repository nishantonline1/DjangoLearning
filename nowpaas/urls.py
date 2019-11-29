from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'products', views.ProductList)
router.register(r'suppliers', views.SupplierList)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_auth_token),
    path('whatsapp',views.whatsAppmsg),
    path('test',views.testsqs)
]
