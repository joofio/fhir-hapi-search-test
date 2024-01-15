import requests

upload_url = "http://localhost:8181/fhir"


def test_search_identifier(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/MedicinalProductDefinition?identifier={mpid}"
    )
    total = response.json()["total"]
    assert total == 1
    # More assertions here based on what you're testing


def test_search_domain(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(upload_url + "/MedicinalProductDefinition?domain=Human")
    total = response.json()["total"]
    assert total == 1
    # More assertions here based on what you're testing


def test_search_name(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url
        + "/MedicinalProductDefinition?name=Equilidem 2.5 mg film-coated tablets"
    )
    total = response.json()["total"]
    assert total == 1
    # More assertions here based on what you're testing


def test_search_language(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(upload_url + "/MedicinalProductDefinition?name-language=en")
    total = response.json()["total"]
    assert total == 1
    # More assertions here based on what you're testing


def test_search_classification(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/MedicinalProductDefinition?product-classification=B01AF02"
    )
    total = response.json()["total"]
    assert total == 1
    # More assertions here based on what you're testing


def test_search_status(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(upload_url + "/MedicinalProductDefinition?status=active")
    total = response.json()["total"]
    assert total == 1
    # More assertions here based on what you're testing


def test_search_type(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/MedicinalProductDefinition?type=MedicinalProduct"
    )
    total = response.json()["total"]
    assert total == 1
    # More assertions here based on what you're testing


def test_search_char_type(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/MedicinalProductDefinition?characteristic-type=color"
    )
    total = response.json()["total"]
    assert total == 1
    # More assertions here based on what you're testing


def test_search_char_value(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/MedicinalProductDefinition?characteristic=white"
    )
    total = response.json()["total"]
    assert total == 1
    # More assertions here based on what you're testing


def test_search_doc_ref(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/MedicinalProductDefinition?master-file=Docexample"
    )
    total = response.json()["total"]
    assert total == 1
    # More assertions here based on what you're testing


def test_search_contact(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/MedicinalProductDefinition?contact=Orgexample"
    )
    total = response.json()["total"]
    assert total == 1
    # More assertions here based on what you're testing


def test_search_ingredient(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/MedicinalProductDefinition?ingredient=paracetamol"
    )
    total = response.json()["total"]
    assert total == 1
    # More assertions here based on what you're testing
