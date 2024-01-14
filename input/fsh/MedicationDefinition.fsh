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
//* attachedDocument = Reference(DocumentReference/example)
//* masterFile = Reference(DocumentReference/example)
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