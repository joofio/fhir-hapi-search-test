# conftest.py

import pytest
import requests
from os import listdir
import json


@pytest.fixture(scope="session")
def upload_file_setup():
    # URL of your server where files need to be uploaded
    upload_url = "http://localhost:8181/fhir"

    # Path to the file you want to upload
    file_path = "/Users/joaoalmeida/Desktop/hl7Europe/gravitate/fhir-hapi-search-test/fsh-generated/resources"
    for file_name in listdir(file_path):
        with open(file_path + "/" + file_name, "r") as file:
            data = json.load(file)
            id_ = data["id"]
            res = data["resourceType"]
            if res == "ImplementationGuide":
                continue
            print(id_, res)

            response = requests.put(upload_url + "/" + res + "/" + id_, json=data)

            if response.status_code not in [200, 201]:
                print(response.status_code)
                pytest.fail(f"Failed to upload file: {response.text}")

    yield

    # Optional: Teardown code after tests are done, like deleting the file
    # ...
    try:
        for file_name in listdir(file_path):
            with open(file_path + "/" + file_name, "r") as file:
                data = json.load(file)
                id_ = data["id"]
                res = data["resourceType"]
        response = requests.delete(
            upload_url + "/" + res + "/" + id_ + "?_cascade=delete"
        )
        response.raise_for_status()  # This will raise an error if the delete request failed
    except requests.RequestException as e:
        print(f"Failed to delete data from server: {e}")


# Your test files would then use this fixture as needed
