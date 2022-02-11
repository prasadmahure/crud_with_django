from django.contrib import admin
from .models import Student

# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
