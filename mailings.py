import csv
import xml.etree.ElementTree as xml


root = xml.Element("shippingAPIRequest")
mailItem = xml.Element("mailItem")
root.append(mailItem)
# If client uses their own label, they need to provide tracking number.
if tracking_number:
    trackingNumber = xml.SubElement(mailItem, "trackingNumber")
    trackingNumber.text = tracking_number

shipperItemID = xml.SubElement(mailItem, "shipperItemID")
shipperItemID.text = shipper_item
displayItemID = xml.SubElement(mailItem, "displayItemID")
displayItemID.text = display_item

# Consignee Properties
consignee = xml.Element("consignee")
mailItem.append(consignee)
name = xml.SubElement(consignee, "name")
name.text = consignee_name
companyname = xml.SubElement(consignee, "companyName")
companyname.text = consignee_company
consignee_street = xml.SubElement(consignee, "addressLine1")
consignee_street.text = con_street_address
consignee_suite = xml.SubElement(consignee, "addressLine2")
consignee_suite.text = con_suite
consignee_city = xml.SubElement(consignee, "city")
consignee_city.text = con_city
consignee_state = xml.SubElement(consignee, "state")
consignee_state.text = con_state
consignee_zip = xml.SubElement(consignee, "zip")
consignee_zip.text = con_zip
consignee_phone = xml.SubElement(consignee, "phone")
consignee_phone.text = con_phone
consignee_email = xml.SubElement(consignee, "email")
consignee_email.text = con_email

#Shipper Properties
shipper = xml.Element("shipper")
mailItem.append(shipper)
shipper_name = xml.SubElement(shipper, "name")
shipper_name.text = shipper_name
shipper_company_name = xml.SubElement(shipper, "companyName")
shipper_company_name.text = shipper_company
shipper_street = xml.SubElement(shipper, "addressLine1")
shipper_street.text = shipper_street_address
shipper_suite = xml.SubElement(shipper, "addressLine2")
shipper_suite.text = shipper_suite
shipper_city = xml.SubElement(shipper, "city")
shipper_city.text = shipper_city
shipper_state = xml.SubElement(shipper, "state")
shipper_state.text = shipper_state
shipper_zip = xml.SubElement(shipper, "zip")
shipper_zip.text = shipper_zip
shipper_phone = xml.SubElement(shipper, "phone")
shipper_phone.text = shipper_phone
shipper_email = xml.SubElement(shipper, "email")
shipper_email.text = shipper_email

# 
if return_address:
    return_address = xml.Element("returnAddress")
    mailItem.append(return_address)
    return_name = xml.SubElement(return_address, "name")
    return_name.text = return_name
    return_company_name = xml.SubElement(return_address, "companyName")
    return_company_name.text = return_company
    return_street = xml.SubElement(return_address, "addressLine1")
    return_street.text = return_street_address
    return_suite = xml.SubElement(return_address, "addressLine2")
    return_suite.text = return_suite
    return_city = xml.SubElement(return_address, "city")
    return_city.text = return_city
    return_state = xml.SubElement(return_address, "state")
    return_state.text = return_state
    return_zip = xml.SubElement(return_address, "zip")
    return_zip.text = return_zip
    return_phone = xml.SubElement(return_address, "phone")
    return_phone.text = return_phone
    return_email = xml.SubElement(return_address, "email")
    return_email.text = return_email  

# Parcel properties
value = xml.Element("value")
value.text = parcel_value
mailItem.append(value)

currency = xml.Element("currency")
currency.text = parcel_currency
mailItem.append(currency)

weight = xml.Element("weight")
weight.text = parcel_weight
mailItem.append(weight)

weightUOM = xml.Element("weightUnitOfMeasure")
weightUOM.text = "kg"
mailItem.append(weightUOM)

dimension = xml.Element("dimensions")
mailItem.append(dimension)
parcel_length = xml.SubElement(dimension, "length")
parcel_length.text = p_length
width = xml.SubElement(dimension, "width")
width.text = parcel_width
height = xml.SubElement(dimension, "height")
height.text = parcel_height

dimensionsUOM = xml.Element("dimensionsUnitOfMeasure")
dimensionsUOM.text = "m"
mailItem.append(dimensionsUOM)

# Parcel Content Properties
product = xml.Element("product")
mailItem.append(product)
country_origin = xml.SubElement(product, "countryOfOrigin")
country_origin.text = parcel_country
harmonization_code = xml.SubElement(product, "harmonizationCode")
harmonization_code.text = hscode
description = xml.SubElement(product, "description")
description.text = product_description
manufacture_code = xml.SubElement(product, "manufacturerCode")
manufacture_code.text = manu_code
sku_code = xml.SubElement(product, "sku")
sku_code.text = sku
quantity = xml.SubElement(product, "quantity")
quantity.text = item_quantity
unit_value = xml.SubElement(product, "unitValue")
unit_value.text = item_value
total_unit_value = xml.SubElement(product, "value")
total_unit_value.text = float(item_value) * int(item_quantity)
unit_weight = xml.SubElement(product, "weight")
unit_weight.text = item_weight
product_URL = xml.SubElement(product, "productURL")
product_URL.text = URL

