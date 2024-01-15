Alias: $WHOAnatomicalTherapeuticChemicalATCClassificationSystem = http://ema.europa.eu/example/WHOAnatomicalTherapeuticChemicalATCClassificationSystem
Alias: $countryCode = http://ema.europa.eu/example/countryCode
Alias: $jurisdictionCode = http://ema.europa.eu/example/jurisdictionCode
Alias: $manufacturingOperationType = http://ema.europa.eu/example/manufacturingOperationType
Alias: $sct = http://snomed.info/sct
Alias: $manufactureddoseform = http://ema.europa.eu/example/manufactureddoseform
Alias: $unitofpresentation = http://ema.europa.eu/example/unitofpresentation
Alias: $v2-0203 = http://terminology.hl7.org/CodeSystem/v2-0203
Alias: $v2-0131 = http://terminology.hl7.org/CodeSystem/v2-0131
Alias: $doseform = http://example.org.uk/fhir/doseform

Instance: MPDexample
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




Instance: MIDexample
InstanceOf: ManufacturedItemDefinition
Usage: #example
* status = #active
* manufacturedDoseForm = $manufactureddoseform#Film-coatedtablet
* unitOfPresentation = $unitofpresentation#Tablet
* manufacturer = Reference(Orgexample)
* property[0].type.coding.code = #shape
* property[=].valueCodeableConcept.text = "Oval"
* property[+].type.coding.code = #color
* property[=].valueCodeableConcept.text = "pink"
* property[+].type.coding.code = #imprint
* property[=].valueCodeableConcept.text = "894"
* name = "ManufatruresdExample"
* ingredient = http://example.org#paracetamol
* identifier.system = "http://ema.europa.eu/example/MID"
* identifier.value = "{mid}"


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



Instance: packagedTest1
InstanceOf: PackagedProductDefinition
Usage: #example


* packageFor = Reference(MPDexample)
* packaging.containedItem[0].item.reference = Reference(MIDexample)
* packaging.containedItem[=].amount = 20 'mL' "ml"



Instance: packagedTest2
InstanceOf: PackagedProductDefinition
Usage: #example
* packaging.containedItem[+].item.reference = Reference(syringeDevice)


Instance: packagedTest3
InstanceOf: PackagedProductDefinition
Usage: #example
* packaging.containedItem[+].item.reference = Reference(allogeneicHCT)

Instance: packagedTest4
InstanceOf: PackagedProductDefinition
Usage: #example
* packaging.containedItem[+].item.reference = Reference(NPexample)





Instance: syringeDevice
InstanceOf: DeviceDefinition
Usage: #example
* classification.type.text = "syringe"




Instance: NPexample
InstanceOf: NutritionProduct
Usage: #example

* code = $sct#227507002
* status = #active
* category = $sct#227313005
* instance.identifier.system = "http://example.org/foodserials"
* instance.identifier.value = "77239487"


Instance: allogeneicHCT
InstanceOf: BiologicallyDerivedProduct
Usage: #example
//* request = Reference(BiologicallyDerivedProduct/HCTcollection-servicerequest) "Service Request for HCT Collection"
* collection.source = Reference(examplePat) "HCT Donor"


Instance: examplePat
InstanceOf: Patient
Usage: #example
* identifier.use = #usual
* identifier.type = $v2-0203#MR
* identifier.system = "urn:oid:1.2.36.146.595.217.0.1"
* identifier.value = "12345"
* identifier.period.start = "2001-05-06"
* identifier.assigner.display = "Acme Healthcare"
* active = true
* name[0].use = #official
* name[=].family = "Chalmers"
* name[=].given[0] = "Peter"
* name[=].given[+] = "James"
* name[+].use = #usual
* name[=].given = "Jim"
* name[+].use = #maiden
* name[=].family = "Windsor"
* name[=].given[0] = "Peter"
* name[=].given[+] = "James"
* name[=].period.end = "2002"
* telecom[0].use = #home
* telecom[+].system = #phone
* telecom[=].value = "(03) 5555 6473"
* telecom[=].use = #work
* telecom[=].rank = 1
* telecom[+].system = #phone
* telecom[=].value = "(03) 3410 5613"
* telecom[=].use = #mobile
* telecom[=].rank = 2
* telecom[+].system = #phone
* telecom[=].value = "(03) 5555 8834"
* telecom[=].use = #old
* telecom[=].period.end = "2014"
* gender = #male
* birthDate = "1974-12-25"
* birthDate.extension.url = "http://hl7.org/fhir/StructureDefinition/patient-birthTime"
* birthDate.extension.valueDateTime = "1974-12-25T14:35:45-05:00"
* deceasedBoolean = false
* address.use = #home
* address.type = #both
* address.text = "534 Erewhon St PeasantVille, Rainbow, Vic  3999"
* address.line = "534 Erewhon St"
* address.city = "PleasantVille"
* address.district = "Rainbow"
* address.state = "Vic"
* address.postalCode = "3999"
* address.period.start = "1974-12-25"
* contact.relationship = $v2-0131#N
* contact.name.family = "du Marché"
* contact.name.family.extension.url = "http://hl7.org/fhir/StructureDefinition/humanname-own-prefix"
* contact.name.family.extension.valueString = "VV"
* contact.name.given = "Bénédicte"
* contact.telecom.system = #phone
* contact.telecom.value = "+33 (237) 998327"
* contact.address.use = #home
* contact.address.type = #both
* contact.address.line = "534 Erewhon St"
* contact.address.city = "PleasantVille"
* contact.address.district = "Rainbow"
* contact.address.state = "Vic"
* contact.address.postalCode = "3999"
* contact.address.period.start = "1974-12-25"
* contact.gender = #female
* contact.period.start = "2012"
