from django.contrib import admin
from .models import Employees # import employee class from models file

# Register your models here.
admin.site.register(Employees)
