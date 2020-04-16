import xml.etree.ElementTree as xml
import csv


def convert_csv_to_manifest_format(csv):

    with open(csv, newline='') as f:
        reader = csv.DictReader(f)

        root = xml.Element("shippingApiRequest")
        manifest = xml.Element("manifest")
        root.append(manifest)

        mawb = xml.SubElement(manifest, "manifestNumber")
        mawb.text = mawb_number