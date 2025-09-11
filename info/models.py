from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()


    def __str__(self):
        return self.question


class Regulations(models.Model):
    content = models.TextField()
    file = models.ImageField(upload_to='Regulations/')

    def __str__(self):
        return "Regulations"


class PrivacyPolicy(models.Model):
    content = models.TextField()
    file = models.ImageField(upload_to='PrivacyPolicy/')
    def __str__(self):
        return "PrivacyPolicy"
