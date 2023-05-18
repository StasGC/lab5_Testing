import unittest
from api_objects import PeopleAPI, PlanetsAPI


class NegativeTestPeopleAPI(unittest.TestCase):
    def setUp(self):
        self.people_api = PeopleAPI()

    def test_get_people_invalid_id(self):
        people_id = 90
        response = self.people_api.get_people(people_id)
        self.assertEqual(response.status_code, 404)


class NegativeTestPlanetsAPI(unittest.TestCase):
    def setUp(self):
        self.planets_api = PlanetsAPI()

    def test_get_planets_invalid_id(self):
        planet_id = 61
        response = self.planets_api.get_planets(planet_id)
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
