import os
from django.core.cache import cache
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .utils import get_common_elements


class FoodInfoView(APIView):
    """
    `/api/paranuara/v1/food_info/<int:people_id>/ (GET)`

    Given 1 people, the API will provide a list of fruits and vegetables they like.
    """
    permission_classes = (AllowAny,)
    queryset = People.objects.all()

    def get(self, request, pk, format=None):
        try:
            person = self.queryset.get(pk=pk)
        except People.DoesNotExist:
            return Response(status=400)
        return Response(FoodInfoSerializer(person).data,
                        status=200)


class SpecialCommonFriendsView(APIView):
    """
    `/api/paranuara/v1/special_common_friends/<int:people_id1>/<int:people_id2>/ (GET)`

    Given 2 people id, the API will provide their information (Name, Age, Address, phone) 
    and the list of their friends in common 
    which have brown eyes and are still alive.
    """
    permission_classes = (AllowAny,)
    queryset = People.objects.all()

    def get_or_set_friends_cache(self, person):
        # get the friend list
        # use cache to increase speed
        f_list = None
        if cache.get(f"{person.pk}_special_friends", None) is not None:
            f_list = cache.get(f"{person.pk}_special_friends")
        else:
            f_list = person.friends.filter(eyeColor="brown",
                                           has_died=False).values_list("id", flat=True)
            # cache for a longer time (1 day)
            cache.set(f"{person.pk}_special_friends", f_list, 24 * 3600)
        return f_list

    def get(self, request, pk1, pk2, format=None):
        try:
            p1 = self.queryset.get(pk=pk1)
            p2 = self.queryset.get(pk=pk2)
        except People.DoesNotExist:
            return Response("Invalid personal id.", status=400)
        f1_list = self.get_or_set_friends_cache(p1)
        f2_list = self.get_or_set_friends_cache(p2)
        id_list = get_common_elements(f1_list, f2_list)
        # retrieve the detail of these friends info
        # common_friends = self.queryset.filter(pk__in=id_list)
        return Response({"person1": PersonalInfoSerializer(p1).data,
                         "person2": PersonalInfoSerializer(p2).data,
                         # retrieve the detail of these common friends info
                         # "special_common_friends": PersonalInfoSerializer(common_friends, many=True).data
                         # retrieve just the id of these friends
                         "special_common_friends": id_list
                         },
                        status=200)


class CompanyEmployeesInfoView(APIView):
    """
    `/api/paranuara/v1/company_employees/<int:company_id>/ (GET)`

    Given a company id, the API returns all their employees' id. 
    """
    permission_classes = (AllowAny,)
    queryset = Companies.objects.all()

    def get(self, request, company_id, format=None):
        try:
            self.queryset.get(pk=company_id)
        except Companies.DoesNotExist:
            return Response("Invalid company id", status=400)
        employees_id = cache.get(f"company_{company_id}", None)
        if employees_id is None:
            employees = People.objects.filter(company__id=company_id)
            employees_id = employees.values_list("id", flat=True)
            cache.set(f"company_{company_id}", employees_id)
        return Response(employees_id, status=200)
        # if we want to get the detail info of employee just uncomment the code below and change the Response
        # employees = People.objects.filter(pk__in=employees_id)
        # serializer = EmployeeSerializer(employees, many=True)
        # return Response(serializer.data, status=200)
