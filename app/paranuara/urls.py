from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    path(r'company_employees/<int:company_id>/', CompanyEmployeesInfoView.as_view()),
    path(r'special_common_friends/<int:pk1>/<int:pk2>/', SpecialCommonFriendsView.as_view()),
    path(r'food_info/<int:pk>/', FoodInfoView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
