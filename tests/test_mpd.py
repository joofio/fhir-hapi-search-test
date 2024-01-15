import requests
import pytest

# Name	Type	Description	Expression	In Common
# dose-form	token	Dose form as manufactured and before any transformation into the pharmaceutical product	ManufacturedItemDefinition.manufacturedDoseForm
# identifier	token	Unique identifier	ManufacturedItemDefinition.identifier
# ingredient	token	An ingredient of this item	ManufacturedItemDefinition.ingredient
# name	token	A descriptive name applied to this item	ManufacturedItemDefinition.name
# status	token	The status of this item. Enables tracking the life-cycle of the content.	ManufacturedItemDefinition.status

upload_url = "http://localhost:8181/fhir"


def test_search_mid_identifier(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(upload_url + "/ManufacturedItemDefinition?identifier={mid}")
    total = response.json()["total"]
    assert total == 1

    # More assertions here based on what you're testing


def test_search_mpd_name(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/ManufacturedItemDefinition?name=ManufatruresdExample"
    )
    total = response.json()["total"]
    assert total == 1

    # More assertions here based on what you're testing


def test_search_mpd_status(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(upload_url + "/ManufacturedItemDefinition?status=active")
    total = response.json()["total"]
    assert total == 1

    # More assertions here based on what you're testing


def test_search_mpd_doseform(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/ManufacturedItemDefinition?dose-form=Film-coatedtablet"
    )
    total = response.json()["total"]
    assert total == 1

    # More assertions here based on what you're testing


def test_search_mpd_ingredient(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/MedicinalProductDefinition?ingredient=paracetamol"
    )
    total = response.json()["total"]
    assert total == 1

    # More assertions here based on what you're testing
