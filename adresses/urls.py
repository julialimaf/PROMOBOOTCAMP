from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CepsViewSet, StatesViewSet, CitiesViewSet

router = DefaultRouter()
router.register(r'ceps', CepsViewSet, basename='ceps')
router.register(r'states', StatesViewSet, basename='states')
router.register(r'cities', CitiesViewSet, basename='cities')

urlpatterns = [
    path('', include(router.urls)),
]
