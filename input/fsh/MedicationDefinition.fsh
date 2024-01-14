Alias: $WHOAnatomicalTherapeuticChemicalATCClassificationSystem = http://ema.europa.eu/example/WHOAnatomicalTherapeuticChemicalATCClassificationSystem
Alias: $countryCode = http://ema.europa.eu/example/countryCode
Alias: $jurisdictionCode = http://ema.europa.eu/example/jurisdictionCode
Alias: $manufacturingOperationType = http://ema.europa.eu/example/manufacturingOperationType

Instance: example
InstanceOf: MedicinalProductDefinition
Usage: #example
* identifier.system = "http://ema.europa.eu/example/MPID"
* identifier.value = "{mpid}"
* domain = http://hl7.org/fhir/medicinal-product-domain#Human

* classification = $WHOAnatomicalTherapeuticChemicalATCClassificationSystem#B01AF02
* masterFile = Reference(Docexample)
* name.productName = "Equilidem 2.5 mg film-coated tablets"
* name.part[0].part = "Equilidem"
* name.part[=].type.coding.code = #INV
* name.part[+].part = "2.5 mg"
* name.part[=].type.coding.code = #STR
* name.part[+].part = "film-coated tablets"
* name.part[=].type.coding.code = #FRM
* name.usage.country = $countryCode#EU
* name.usage.jurisdiction = $jurisdictionCode#EU
* name.usage.language = urn:ietf:bcp:47#en
* operation.type.concept = $manufacturingOperationType#Batchrelease
* operation.effectiveDate.start = "2013-03-15"
* type = http://hl7.org/fhir/medicinal-product-type#MedicinalProduct
* status = http://hl7.org/fhir/publication-status#active
* characteristic.type = http://example.org#color
* characteristic.valueCodeableConcept = http://example.org#white
* contact.contact = Reference(Orgexample)
* ingredient = http://example.org#paracetamol


Instance: Docexample
InstanceOf: DocumentReference
Usage: #example

* status =  http://hl7.org/fhir/document-reference-status#current
* content.attachment.language = urn:ietf:bcp:47#en



Instance: Orgexample
InstanceOf: Organization
Usage: #example


* active = true
* name = "stuff"