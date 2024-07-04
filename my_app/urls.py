from django.urls import path, include
from .views  import *
from rest_framework import routers

app_name = 'my_app'

router = routers.DefaultRouter()
router.register('hududlar', HududlarViewSet),
router.register('kompaniyalar', KompaniyalarViewSet),
router.register('binolar', BinolarViewSet),



urlpatterns = [
    path('my_app/', include(router.urls)),
    ]