import requests

url = 'https://acpapi.com/API/'
labels = {
            'None': 0,
            'Ground': 1,
            'Expedited': 2,
            'Expedited Max': 4,
            'Priority': 3,
        }
label_formats = ['PNG', 'PDF', 'EPL2', None]


def create_mailing(xml, apikey, test_mode=0, label='None', label_format=None):
    
    parameters = {
                    'apikey': apikey,
                    'command': 'createMailing',
                    'testMode': test_mode,
                    'data': xml,
                    'label': label,
                    'labelFormat': label_format,
                }
    if label in labels.keys():
        r = requests.post(url, parameters)
    return r.content, r.status_code


def delete_mailing(apikey, tracking_number, shipperitemid=None):
    xml = f'''<?xml version="1.0" encoding="utf-8" ?> 
                <shippingApiRequest>
                    <mailItem>
                        <trackingNumber>{tracking_number}</trackingNumber>
                        <shipperItemId>{shipperitemid}</shipperItemId>
                    </mailItem>
                </shippingApiRequest>'''
    parameters = {
        'apikey': apikey,
        'command': 'cancelMailing',
        'data': xml,
    }
    r = requests.post(url, parameters)
    return r.content, r.status_code


def create_bag(apikey, tracking_number, bag_id=None, comment=None,
    shipper_item_id=None, label=0, label_format='PNG'):
    xml = f'''<?xml version="1.0" encoding="utf-8" ?> 
                <shippingApiRequest>
                    <bag>
                        <shipperBagId>{bag_id}</shipperBagId>
                        <comment>{comment}</comment>
                        <mailItem>
                            <trackingNumber>{tracking_number}</trackingNumber>
                            <shipperItemId>{shipper_item_id}</shipperItemId>
                        </mailItem>
                    </bag>
                </shippingApiRequest>'''
    parameters = {
        'apikey': apikey,
        'command': 'createBag',
        'data': xml,
        'label': label,
        'labelFormat': label_format,
    }
    r = requests.post(url, parameters)
    return r.content, r.status_code

def cancel_bag(apikey, bag_id, shipper_bag_id)
