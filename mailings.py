import xml.etree.ElementTree as xml
import csv


def convert_csv_to_ACPAPI_format(csv):
    with open(csv, newline='') as f:
        reader = csv.DictReader(f)
    
        for line in reader:
            if line['ï»¿trackingNumber'] == 'ï»¿trackingNumber':
                continue
    
            root = xml.Element("shippingApiRequest")
            mailItem = xml.Element("mailItem")
            root.append(mailItem)
            # If client uses their own label, they need to provide tracking number.
            if line['ï»¿trackingNumber']:
                trackingNumber = xml.SubElement(mailItem, "trackingNumber")
                trackingNumber.text = line['ï»¿trackingNumber']
            
            shipperItemID = xml.SubElement(mailItem, "shipperItemId")
            shipperItemID.text = line['shipperItemId']
            displayItemID = xml.SubElement(mailItem, "displayItemId")
            displayItemID.text = line['displayItemId']
            
            # Consignee Properties
            consignee = xml.Element("consignee")
            mailItem.append(consignee)
            name = xml.SubElement(consignee, "name")
            name.text = line['consigneeName']
            companyname = xml.SubElement(consignee, "companyName")
            companyname.text = line['consigneeCompanyName']
            consignee_street = xml.SubElement(consignee, "addressLine1")
            consignee_street.text = line['consigneeAddressLine1']
            consignee_suite = xml.SubElement(consignee, "addressLine2")
            consignee_suite.text = line['consigneeAddressLine2']
            consignee_city = xml.SubElement(consignee, "city")
            consignee_city.text = line['consigneeCity']
            consignee_state = xml.SubElement(consignee, "state")
            consignee_state.text = line["consigneeState"]
            consignee_zip = xml.SubElement(consignee, "zip")
            consignee_zip.text = line["consigneeZip"]
            consignee_country = xml.SubElement(consignee, "country")
            consignee_country.text = line["consigneeCountry"]
            consignee_phone = xml.SubElement(consignee, "phone")
            consignee_phone.text = line["consigneePhone"]
            consignee_email = xml.SubElement(consignee, "email")
            consignee_email.text = line["consigneeEmail"]
            
            #Shipper Properties
            shipper = xml.Element("shipper")
            mailItem.append(shipper)
            shipper_name = xml.SubElement(shipper, "name")
            shipper_name.text = line["shipperName"]
            shipper_company_name = xml.SubElement(shipper, "companyName")
            shipper_company_name.text = line["shipperCompanyName"]
            shipper_street = xml.SubElement(shipper, "addressLine1")
            shipper_street.text = line["shipperAddressLine1"]
            shipper_suite = xml.SubElement(shipper, "addressLine2")
            shipper_suite.text = line["shipperAddressLine2"]
            shipper_city = xml.SubElement(shipper, "city")
            shipper_city.text = line["shipperCity"]
            shipper_state = xml.SubElement(shipper, "state")
            shipper_state.text = line["shipperState"]
            shipper_zip = xml.SubElement(shipper, "zip")
            shipper_zip.text = line["shipperZip"]
            shipper_country = xml.SubElement(shipper, "country")
            shipper_country.text = line["shipperCountry"]
            shipper_phone = xml.SubElement(shipper, "phone")
            shipper_phone.text = line["shipperPhone"]
            shipper_email = xml.SubElement(shipper, "email")
            shipper_email.text = line["shipperEmail"]
            shipper_URL = xml.SubElement(shipper, "shipperURL")
            shipper_URL.text = line["shipperURL"]
            
            # 
            # if return_address:
            #     return_address = xml.Element("returnAddress")
            #     mailItem.append(return_address)
            #     return_name = xml.SubElement(return_address, "name")
            #     return_name.text = return_name
            #     return_company_name = xml.SubElement(return_address, "companyName")
            #     return_company_name.text = return_company
            #     return_street = xml.SubElement(return_address, "addressLine1")
            #     return_street.text = return_street_address
            #     return_suite = xml.SubElement(return_address, "addressLine2")
            #     return_suite.text = return_suite
            #     return_city = xml.SubElement(return_address, "city")
            #     return_city.text = return_city
            #     return_state = xml.SubElement(return_address, "state")
            #     return_state.text = return_state
            #     return_zip = xml.SubElement(return_address, "zip")
            #     return_zip.text = return_zip
            #     return_phone = xml.SubElement(return_address, "phone")
            #     return_phone.text = return_phone
            #     return_email = xml.SubElement(return_address, "email")
            #     return_email.text = return_email  
            
            # Parcel properties
            value = xml.Element("value")
            value.text = line["value"]
            mailItem.append(value)
            
            currency = xml.Element("currency")
            currency.text = line["currency"]
            mailItem.append(currency)
            
            weight = xml.Element("weight")
            weight.text = line["weight"]
            mailItem.append(weight)
            
            weightUOM = xml.Element("weightUnitOfMeasure")
            weightUOM.text = "kg"
            mailItem.append(weightUOM)
            
            dimension = xml.Element("dimensions")
            mailItem.append(dimension)
            parcel_length = xml.SubElement(dimension, "length")
            parcel_length.text = line["dimensionsLength"]
            width = xml.SubElement(dimension, "width")
            width.text = line["dimensionsWidth"]
            height = xml.SubElement(dimension, "height")
            height.text = line["dimensionsHeight"]
            
            dimensionsUOM = xml.Element("dimensionsUnitOfMeasure")
            dimensionsUOM.text = "m"
            mailItem.append(dimensionsUOM)
            
            # Parcel Content Properties
            product = xml.Element("product")
            mailItem.append(product)
            country_origin = xml.SubElement(product, "countryOfOrigin")
            country_origin.text = line["productCountryOfOrigin"]
            harmonization_code = xml.SubElement(product, "harmonizationCode")
            harmonization_code.text = line["productHarmonizationCode"]
            description = xml.SubElement(product, "description")
            description.text = line["productDescription"]
            manufacture_code = xml.SubElement(product, "manufacturerCode")
            manufacture_code.text = line["productManufacturerCode"]
            sku_code = xml.SubElement(product, "sku")
            sku_code.text = line["productSku"]
            quantity = xml.SubElement(product, "quantity")
            quantity.text = line["productQuantity"]
            unit_value = xml.SubElement(product, "unitValue")
            unit_value.text = line["productValue"]
            total_unit_value = xml.SubElement(product, "value")
            total_unit_value.text = line["productValue"]
            unit_weight = xml.SubElement(product, "weight")
            unit_weight.text = line["weight"]
            product_URL = xml.SubElement(product, "productURL")
            product_URL.text = line["productURL"]
            PNFN = xml.Element("priorNoticeFilingNumber")
            PNFN.text = ""
            mailItem.append(PNFN)
    
            return xml.tostring(root, encoding='utf8').decode('utf8')
    
            # print(acpapi.create_mailing(tree, '8557d4855241ba2d'))
            # with open('test.xml', 'w') as f:
            #     f.write(tree)
    
    