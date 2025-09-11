from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LuckyNumberView

router = DefaultRouter()
router.register(r'luckynumber', LuckyNumberView, basename='lucky-numbers')

urlpatterns = [
    path('', include(router.urls)),
]
