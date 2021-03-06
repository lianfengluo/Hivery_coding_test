"""Accommodation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


# router:
urlpatterns = [
    path(r"api/paranuara/v1/", include("paranuara.urls")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
