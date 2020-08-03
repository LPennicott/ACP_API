import sys
import requests
import PySimpleGUI as sg
import mailings

url = "https://acpapi.com/API/"
labels = {
    "None": 0,
    "Ground": 1,
    "Expedited": 2,
    "Expedited Max": 4,
    "Priority": 3,
}
label_formats = [
    "PNG",
    "PDF",
    "EPL2",
]


def create_mailing(csv, apikey, test_mode=1, label="None", label_format="PNG"):

    xml = mailings.convert_csv_to_ACPAPI_format(csv)
    # If label_format not valid, default to PNG
    if label_format not in label_formats:
        label_format = "PNG"
    # Options for API create mailing command
    parameters = {
        "apikey": apikey,
        "command": "createMailing",
        "testMode": test_mode,
        "data": xml,
        # If label selection not valid, default to no label
        "label": labels.get(label, "None"),
        "labelFormat": label_format,
    }
    r = requests.post(url, parameters)
    return r.content, r.status_code


def delete_mailing(apikey, tracking_number, shipperitemid=None):
    xml = f"""<?xml version="1.0" encoding="utf-8" ?>
                <shippingApiRequest>
                    <mailItem>
                        <trackingNumber>{tracking_number}</trackingNumber>
                        <shipperItemId>{shipperitemid}</shipperItemId>
                    </mailItem>
                </shippingApiRequest>
            """
    parameters = {
        "apikey": apikey,
        "command": "cancelMailing",
        "data": xml,
    }
    r = requests.post(url, parameters)
    return r.content, r.status_code


def create_bag(
    apikey,
    tracking_number,
    bag_id=None,
    comment=None,
    shipper_item_id=None,
    label=0,
    label_format="PNG",
):
    xml = f"""<?xml version="1.0" encoding="utf-8" ?>
                <shippingApiRequest>
                    <bag>
                        <shipperBagId>{bag_id}</shipperBagId>
                        <comment>{comment}</comment>
                        <mailItem>
                            <trackingNumber>{tracking_number}</trackingNumber>
                            <shipperItemId>{shipper_item_id}</shipperItemId>
                        </mailItem>
                    </bag>
                </shippingApiRequest>"""
    parameters = {
        "apikey": apikey,
        "command": "createBag",
        "data": xml,
        "label": label,
        "labelFormat": label_format,
    }
    r = requests.post(url, parameters)
    return r.content, r.status_code


def cancel_bag(apikey, bag_id, shipper_bag_id):
    xml = f"""<?xml version="1.0" encoding="utf-8" ?>
                <shippingApiRequest>
                    <bag>
                        <bagId>{bag_id}</bagId>
                        <shipperBagId>{shipper_bag_id}</shipperBagId>
                    </bag>
                </shippingApiRequest>"""
    parameters = {
        "apikey": apikey,
        "command": "cancelBag",
        "data": xml,
    }
    r = requests.post(url, parameters)
    return r.content, r.status_code


def create_manifest(apikey, csv, clearance_type):

    pass

