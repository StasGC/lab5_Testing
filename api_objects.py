import requests


class BaseAPI:
    def __init__(self):
        self.base_url = "https://swapi.dev/api/"

    def make_request(self, resource, resource_id=None):
        url = f"{self.base_url}{resource}/"
        if resource_id:
            url += f"{resource_id}/"
        response = requests.get(url)
        return response


class PeopleAPI(BaseAPI):
    def __init__(self):
        super().__init__()

    def get_people(self, people_id):
        return self.make_request(resource="people", resource_id=people_id)


class PlanetsAPI(BaseAPI):
    def __init__(self):
        super().__init__()

    def get_planets(self, planets_id):
        return self.make_request(resource="planets", resource_id=planets_id)
