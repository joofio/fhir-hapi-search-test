import requests

# Name	Type	Description	Expression	In Common
# biological	reference	A biologically derived product within this packaged product	PackagedProductDefinition.packaging.containedItem.item.reference
# contained-item	reference	Any of the contained items within this packaged product	PackagedProductDefinition.packaging.containedItem.item.reference
# device	reference	A device within this packaged product	PackagedProductDefinition.packaging.containedItem.item.reference
# identifier	token	Unique identifier	PackagedProductDefinition.identifier
# manufactured-item	reference	A manufactured item of medication within this packaged product	PackagedProductDefinition.packaging.containedItem.item.reference
# medication	reference	A manufactured item of medication within this packaged product	PackagedProductDefinition.packaging.containedItem.item.reference
# name	token	A name for this package. Typically what it would be listed as in a drug formulary or catalogue, inventory etc.	PackagedProductDefinition.name
# nutrition	reference	A nutrition product within this packaged product	PackagedProductDefinition.packaging.containedItem.item.reference
# package	reference	A complete packaged product within this packaged product	PackagedProductDefinition.packaging.containedItem.item.reference
# package-for	reference	The product that this is a pack for	PackagedProductDefinition.packageFor(MedicinalProductDefinition)
# status	token	The status within the lifecycle of this item. A high level status, this is not intended to duplicate details carried elsewhere such as legal status, or authorization or marketing status	PackagedProductDefinition.status

upload_url = "http://localhost:8181/fhir"


def test_search_ppd_biological(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/PackagedProductDefinition?biological=NPexample"
    )
    total = response.json()["total"]
    assert total == 1


def test_search_ppd_nutrition(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/PackagedProductDefinition?nutrition=allogeneicHCT"
    )
    total = response.json()["total"]
    assert total == 1


def test_search_ppd_device(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/PackagedProductDefinition?device=syringeDevice"
    )
    total = response.json()["total"]
    assert total == 1


def test_search_ppd_mid(upload_file_setup):
    # Test some functionality after setup
    response = requests.get(
        upload_url + "/PackagedProductDefinition?manufactured-item=MIDexample"
    )
    total = response.json()["total"]
    assert total == 1
