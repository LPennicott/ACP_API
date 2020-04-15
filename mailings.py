import csv
import xml.etree.ElementTree as xml


root = xml.Element("shippingAPIRequest")
mailItem = xml.Element("mailItem")
root.append(mailItem)
# If client uses their own label, they need to provide tracking number.
if tracking_number:
    trackingNumber = xml.SubElement(mailItem, "trackingNumber")
    trackingNumber.text = f"{tracking_number}"

shipperItemID = xml.SubElement(mailItem, "shipperItemID")
shipperItemID.text = f"{shipper_item}"
displayItemID = xml.SubElement(mailItem, "displayItemID")
displayItemID.text = f"{display_item}"

consignee = xml.Element("consignee")
mailItem.append(consignee)
name = xml.SubElement(consignee, "name")
name.text = f"{consignee_name}"
companyname = xml.SubElement(consignee, "companyName")
companyname.text = f"{consignee_company}"