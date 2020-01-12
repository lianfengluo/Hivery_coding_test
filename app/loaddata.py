import dateutil.parser
import json
from paranuara.models import *
import datetime
import re


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

print("Finished loading companies data.", flush=True)
print("Start loading people data.", flush=True)

# load people info
with open("resources/people.json") as json_file:
    data = json.load(json_file)
    for d in data:
      # used for storing as the datetime field
      registered = dateutil.parser.parse(d["registered"])
      vegetables, fruits = [], []
      # mapping the favouriteFood to vegetable or fruit.
      for food in d["favouriteFood"]:
        if food_type[food] == "vegetable":
          vegetables.append(food)
        else:
          fruits.append(food)
      try:
        People(pk=d["index"], _id=d["_id"], guid=d["guid"], has_died=d["has_died"], 
              balance=float(re.sub(r'[^\d.]', '', d["balance"])), picture=d["picture"], age=d["age"], 
              eyeColor=d["eyeColor"], name=d["name"], 
              gender="f" if d["gender"][0] == "f" else "m", 
              company_id=d["company_id"], email=d["email"], phone=d["phone"], 
              address=d["address"], about=d["about"], 
              registered=registered, tags=d["tags"], greeting=d["greeting"],
              vegetables=vegetables, fruits=fruits
              ).save()
      except:
        # If the database structure is not compatible, then just skip.
        pass
    print("Finished loading people data.", flush=True)
    print("Start loading friends data.", flush=True)
    for d in data:
      try:
        p = People.objects.get(pk=d["index"])
        p.friends.set(list(map(lambda x: x["index"], d["friends"])))
        p.save()
      except:
        # if person is and invalid index do not do anything
        # Or index does not exist
        pass
print("Finished data loading.", flush=True)