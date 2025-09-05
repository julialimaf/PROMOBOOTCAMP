from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.FaqListView.as_view(), name='faq-list'),
    path('regulations/', views.RegulationsView.as_view(), name='regulations'),
    path('policy/', views.PrivacyPolicyView.as_view(), name='policy'),
]
