# myapp/admin.py
from django.contrib import admin
from .models import Member  # Import your model

admin.site.register(Member)  # Register your model with the admin site
