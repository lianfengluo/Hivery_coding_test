from django.test import TestCase
from rest_framework.test import APIClient
from .models import *
import json
import random


class ApiTest(TestCase):
    """ Test module for api """
    fixtures = ['test.json']

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        with open("resources/companies.json") as json_file:
            self.companies = json.load(json_file)
        with open("resources/people.json") as json_file:
            self.people = json.load(json_file)
        self.food_type = {}
        # load food type
        with open("resources/food_classes.json") as json_file:
            data = json.load(json_file)
            for d in data:
                self.food_type[d["food"]] = d["kind"]

    def test_companies_employee(self):
        # print("start testing /api/paranuara/v1/company_employees/<int:company_id>/", flush=True)
        # random test 10 time if the length of the companies list greater or equal to 10
        num_of_test = 10 if len(self.companies) > 10 else len(self.companies)
        random_company_id_list = []
        while len(random_company_id_list) < num_of_test:
            index = random.choice(self.companies)["index"]
            if index not in random_company_id_list:
                random_company_id_list.append(index)
        random_company_id_set = set(random_company_id_list)
        employees_id_list = [[] for _ in range(num_of_test)]
        for p in self.people:
            if p["company_id"] in random_company_id_set:
                list_pos = random_company_id_list.index(p["company_id"])
                employees_id_list[list_pos].append(p["index"])
        for i, company_id in enumerate(random_company_id_list):
            response = self.client.get(
                f'/api/paranuara/v1/company_employees/{company_id}/')
            response_people_indices = set(json.loads(response.content))
            self.assertEqual(response_people_indices,
                             set(employees_id_list[i]))

    def test_special_friends(self):
        # print("Start testing /api/paranuara/v1/special_common_friends/<int:people_id1>/<int:people_id2>/", flush=True)
        num_of_test = 10
        random_people_pair_list = [(random.choice(self.people),
                                    random.choice(self.people)) for _ in range(num_of_test)]
        for r_p1, r_p2 in random_people_pair_list:
            r_id1, r_id2 = r_p1["index"], r_p2["index"]
            response = self.client.get(
                f'/api/paranuara/v1/special_common_friends/{r_id1}/{r_id2}/')
            resp = json.loads(response.content)
            # (Name, Age, Address, phone)
            info1 = {"name": r_p1["name"], "age": r_p1["age"], "address": r_p1["address"],
                     "phone": r_p1["phone"]}
            info2 = {"name": r_p2["name"], "age": r_p2["age"], "address": r_p2["address"],
                     "phone": r_p2["phone"]}
            self.assertEqual(resp["person1"], info1)
            self.assertEqual(resp["person2"], info2)
            r_p1_s_f = People.objects.filter(pk__in=set(map(lambda x: x["index"], r_p1["friends"])),
                                             eyeColor="brown", has_died=False).values_list("id", flat=True)
            r_p2_s_f = People.objects.filter(pk__in=set(map(lambda x: x["index"], r_p2["friends"])),
                                             eyeColor="brown", has_died=False).values_list("id", flat=True)
            special_common_friends = set(r_p1_s_f).intersection(r_p2_s_f)
            self.assertEqual(
                set(resp["special_common_friends"]), special_common_friends)

    def test_favourite_fruit(self):
        # print("Start testing /api/paranuara/v1/food_info/<int:people_id>/", flush=True)
        num_of_test = 10
        random_people_list = [random.choice(
            self.people) for _ in range(num_of_test)]
        for r_p in random_people_list:
            vegetables, fruits = [], []
            # generate the formatted test data
            for food in r_p["favouriteFood"]:
                if self.food_type[food] == "vegetable":
                    vegetables.append(food)
                else:
                    fruits.append(food)
            test_data = {"username": r_p["name"], "age": str(r_p["age"]),
                         "fruits": fruits, "vegetables": vegetables}
            response = self.client.get(
                f'/api/paranuara/v1/food_info/{r_p["index"]}/')
            resp = json.loads(response.content)
            self.assertEqual(test_data, resp)
