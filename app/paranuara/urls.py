from .views import *
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(r'company_employees/<int:company_id>/', CompanyEmployeeView.as_view()),
    path(r'special_common_friends/<int:pk1>/<int:pk2>/', BrownEyeCommonFriendsView.as_view()),
    path(r'food_info/<int:pk>/', FoodInfoView.as_view()),
]

