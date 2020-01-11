import dateutil.parser
import json
from paranuara.models import *
import datetime


food_type = {}
# load food type
with open("resources/food_classes.json") as json_file:
  data = json.load(json_file)
  for d in data:
    food_type[d["food"]] = d["kind"]

# load companies info
with open("resources/companies.json") as json_file:
    data = json.load(json_file)
    for d in data:
      Companies(pk=d["index"], name=d["company"]).save()

# load people info
with open("resources/people.json") as json_file:
    data = json.load(json_file)
    for d in data:
      # used for storing as the datetime field
      # registered = dateutil.parser.parse(d["registered"])
      vegetables, fruits = [], []
      for food in d["favouriteFood"]:
        if food_type[food] == "vegetable":
          vegetables.append(food)
        else:
          fruits.append(food)
      try:
        People(pk=d["index"], _id=d["_id"], guid=d["guid"], has_died=d["has_died"], 
              balance=float(d["balance"][1:].replace(",", "")), picture=d["picture"], age=d["age"], 
              eyeColor=d["eyeColor"],  name=d["name"], 
              gender= "f" if d["gender"][0] == "f" else "m", 
              company_id=d["company_id"], email=d["email"], phone=d["phone"], 
              address=d["address"], about=d["about"], 
              registered=d["registered"], tags=d["tags"], greeting=d["greeting"],
              vegetables=vegetables, fruits=fruits
              ).save()
      except:
        # If the database structure is not compatible, then just skip.
        pass
    for d in data:
      try:
        p = People.objects.get(pk=d["index"])
        for index in d["friends"]:
          p.friends.add(index["index"])
        p.save()
      except:
        # if person is and invalid index do not do anything
        # Or index does not exist
        pass