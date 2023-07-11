from django.contrib import admin

# Register your models here.

# give access to admin to your models

from .models import Question, Choice

admin.site.register(Question)
