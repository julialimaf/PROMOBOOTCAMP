from django.contrib import admin
from .models import Faq, Regulations, PrivacyPolicy

admin.site.register(Faq)
admin.site.register(Regulations)
admin.site.register(PrivacyPolicy)
