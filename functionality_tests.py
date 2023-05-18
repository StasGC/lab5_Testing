import unittest
from api_objects import PeopleAPI, PlanetsAPI


class FunctionalityTestPeopleAPI(unittest.TestCase):
    def setUp(self):
        self.people_api = PeopleAPI()

    def test_get_people_valid_id(self):
        people_id = 1
        response = self.people_api.get_people(people_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Luke Skywalker')


class FunctionalityTestPlanetsAPI(unittest.TestCase):
    def setUp(self):
        self.planets_api = PlanetsAPI()

    def test_get_planets_valid_id(self):
        planet_id = 1
        response = self.planets_api.get_planets(planet_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Tatooine')


if __name__ == "__main__":
    unittest.main()
