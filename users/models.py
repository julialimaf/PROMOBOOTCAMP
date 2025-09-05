from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)  
    first_name = models.CharField("First Name", max_length=150)
    last_name = models.CharField("Last Name", max_length=150)
    email = models.EmailField("Email", unique=True)
    phone = models.CharField("Phone", max_length=20, blank=True)
    address_state = models.CharField("State", max_length=50)
    address_city = models.CharField("City", max_length=50)
    address_zip = models.CharField("ZIP Code", max_length=10)
    password = models.CharField("Password", max_length=128)    
    
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return f"{self.cpf} - {self.first_name}"
