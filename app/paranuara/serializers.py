from .models import *
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the employee personal info
    """
    gender = serializers.SerializerMethodField()

    def get_gender(self,obj):
        return obj.get_gender_display()

    def to_representation(self, instance):
         # instance is the model object. create the custom json format by accessing instance attributes normaly and return it
        representation = super(EmployeeSerializer, self).to_representation(instance)
        representation["balance"] = "$" + str(instance.balance)

        return representation

    class Meta:
        model = People
        fields = "__all__"

class PersonalInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ("name", "age", "address", "phone",)

class FoodInfoSerializer(serializers.ModelSerializer):
    """
    food perference info
    """
    username = serializers.CharField(source="name")

    def to_representation(self, instance):
        #  convert the age from int type to str type
        representation = super(FoodInfoSerializer, self).to_representation(instance)
        representation["age"] = str(instance.age)

        return representation

    class Meta:
        model = People
        fields = ("username", "age", "fruits", "vegetables",)