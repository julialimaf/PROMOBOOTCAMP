from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.FaqListView.as_view(), name='faq-list'),
    path('regulamento/', views.RegulamentoView.as_view(), name='regulamento'),
    path('politica/', views.PoliticaPrivacidadeView.as_view(), name='politica'),
]
