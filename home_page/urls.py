from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from home_page import views

urlpatterns = [
    path("", views.index, name='home'),
    # path("update", views.update, name='update'),
    path("delete/<int:id>/", views.delete_data, name='deletedata'),
    path("update<int:id>/", views.update_data, name='updatedata'),
    # path("services", views.services, name='services')
]