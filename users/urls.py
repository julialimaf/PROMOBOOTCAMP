from django.urls import path
from .views import RegisterView, LoginView, MydataView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('mydata/', MydataView.as_view(), name='mydata'),  
]
