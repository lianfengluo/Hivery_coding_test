from .models import *
from rest_framework import serializers

# This class is for fully employee's info
class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the employee personal info with all fields
    """
    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
        return obj.get_gender_display()

    def to_representation(self, instance):
         # convert the float point number back to the currency format
        representation = super(
            EmployeeSerializer, self).to_representation(instance)
        representation["balance"] = f"${instance.balance:,.2f}"

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
        representation = super(
            FoodInfoSerializer, self).to_representation(instance)
        representation["age"] = str(instance.age)

        return representation

    class Meta:
        model = People
        fields = ("username", "age", "fruits", "vegetables",)
