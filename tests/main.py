import unittest
import requests
from os import listdir
import json

SERVER = "http://localhost:8181/fhir"
FOLDER = "/Users/joaoalmeida/Desktop/hl7Europe/gravitate/fhir-hapi-search-test/fsh-generated/resources"


class ServerTest(unittest.TestCase):
    def setUp(self):
        # Upload JSON files to the server
        self.upload_url = SERVER
        self.folder = FOLDER

        for file_name in listdir(self.folder):
            with open(self.folder + "/" + file_name, "r") as file:
                data = json.load(file)
                id_ = data["id"]
                res = data["resourceType"]
                if res == "ImplementationGuide":
                    continue
                print(id_, res)

                response = requests.put(
                    self.upload_url + "/" + res + "/" + id_, json=data
                )
                print(response)

    def test_search_identifier(self):
        # Test some functionality after setup
        response = requests.get(
            self.upload_url + "/MedicinalProductDefinition?identifier={mpid}"
        )
        total = response.json()["total"]
        self.assertEqual(total, 1)
        # More assertions here based on what you're testing

    def test_search_domain(self):
        # Test some functionality after setup
        response = requests.get(
            self.upload_url + "/MedicinalProductDefinition?domain=Human"
        )
        total = response.json()["total"]
        self.assertEqual(total, 1)
        # More assertions here based on what you're testing

    def test_search_name(self):
        # Test some functionality after setup
        response = requests.get(
            self.upload_url
            + "/MedicinalProductDefinition?name=Equilidem 2.5 mg film-coated tablets"
        )
        total = response.json()["total"]
        self.assertEqual(total, 1)
        # More assertions here based on what you're testing

    def test_search_language(self):
        # Test some functionality after setup
        response = requests.get(
            self.upload_url + "/MedicinalProductDefinition?name-language=en"
        )
        total = response.json()["total"]
        self.assertEqual(total, 1)
        # More assertions here based on what you're testing

    def test_search_classification(self):
        # Test some functionality after setup
        response = requests.get(
            self.upload_url
            + "/MedicinalProductDefinition?product-classification=B01AF02"
        )
        total = response.json()["total"]
        self.assertEqual(total, 1)
        # More assertions here based on what you're testing

    def test_search_status(self):
        # Test some functionality after setup
        response = requests.get(
            self.upload_url + "/MedicinalProductDefinition?status=active"
        )
        total = response.json()["total"]
        self.assertEqual(total, 1)
        # More assertions here based on what you're testing

    def test_search_type(self):
        # Test some functionality after setup
        response = requests.get(
            self.upload_url + "/MedicinalProductDefinition?type=MedicinalProduct"
        )
        total = response.json()["total"]
        self.assertEqual(total, 1)
        # More assertions here based on what you're testing


if __name__ == "__main__":
    unittest.main()
