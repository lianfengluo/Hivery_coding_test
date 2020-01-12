from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Companies(models.Model):
    """
    Model for the company table
    """
    name = models.CharField(null=False, max_length=500)

    class Meta:
        db_table = "Companies"
        verbose_name_plural = "Companies"

class People(models.Model):
    """
    Model for the Person table
    """
    Genders = (
        ("m", "male"),
        ("f", "female")
    )
    _id = models.CharField(null=False, max_length=24)
    guid = models.CharField(null=False, max_length=36)
    has_died = models.BooleanField(null=False)
    balance = models.FloatField(default=0.0)
    picture = models.URLField(max_length=300)
    age = models.IntegerField()
    eyeColor = models.CharField(max_length=20)
    name = models.CharField(null=False, max_length=100)
    gender = models.CharField(
        max_length=1, choices=Genders, null=False)
    company = models.ForeignKey(Companies,
                                null=True,
                                db_constraint=False,
                                on_delete=models.SET_NULL)
    email = models.EmailField(null=False)
    phone = models.CharField(null=False, max_length=50)
    address = models.CharField(null=False, max_length=500)
    about = models.TextField()
    # If we want to store as the datetime
    registered = models.DateTimeField(null=False)
    tags = ArrayField(
        base_field=models.CharField(max_length=30),
        size= 7,
        max_length=(7 * 31)  # 7 * 30 character nominals, plus commas
    )
    greeting = models.CharField(max_length=300)
    friends = models.ManyToManyField("self", symmetrical=False)
    vegetables = ArrayField(
        base_field=models.CharField(max_length=20),
        size=4,
        max_length=(4 * 21)  # 4 * 20 character nominals, plus commas
    )
    fruits = ArrayField(
        base_field=models.CharField(max_length=20),
        size=4,
        max_length=(4 * 21)  # 4 * 20 character nominals, plus commas
    )

    class Meta:
        db_table = "People"
        verbose_name_plural = "People"

