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
    path(r"api/paranuara/", include("paranuara.urls")),
]
