import csv


mailing = f"""<?xml version="1.0" encoding="utf-8" ?> 
                <shippingApiRequest>

                    <mailItem>
                        <!-- NOTE: transmit field 'trackingNumber' ONLY if you print shipping labels yourself -->
                        <trackingNumber>{tracking}</trackingNumber>
                        <shipperItemId>{shipperItemId}</shipperItemId>
                        <displayItemId>{displayItemId}</displayItemId>
                
                        <consignee>
                            <name>{name}</name>
                            <companyName />
                            <addressLine1>{street}</addressLine1>
                            <addressLine2>{suite}</addressLine2>
                            <city>{city}</city>
                            <state>{state}</state>
                            <zip>{zipcode}</zip>
                            <country>US</country>
                            <phone>{phone}</phone>
                            <email>{email}</email>
                        </consignee>
                
                        <shipper>
                            <name>{shipper_name}</name>
                            <companyName>{company_name}</companyName>
                            <addressLine1>{shipper_address}</addressLine1>
                            <addressLine2>{shipper_suite}</addressLine2>
                            <city>{shipper_city}</city>
                            <state>{shipper_state}</state>
                            <zip>{shipper_zip}</zip>
                            <country>{shipper_country}</country>
                            <phone></phone>
                            <email>{shipper_email}</email>
                            <shipperURL>{shipper_url}</shipperURL>
                        </shipper>
                        
                        <returnAddress>
                            <name>John Smith</name>
                            <companyName>Shippers, LLC</companyName>
                            <addressLine1>LAX</addressLine1>
                            <addressLine2 />
                            <city>Los Angeles</city>
                            <state>CA</state>
                            <zip>90045</zip>
                            <country>US</country>
                            <phone>1 (800) 426-4968</phone>
                            <email>john-smith@gmail.com</email>
                        </returnAddress>

                        <value>100.50</value>
                        <currency>EUR</currency>
                        <weight>1.125</weight>
                        <weightUnitOfMeasure>kg</weightUnitOfMeasure>
                        <dimensions>
                            <length>0.5</length>
                            <width>0.4</width>
                            <height>0.3</height>
                        </dimensions>
                        <dimensionsUnitOfMeasure>m</dimensionsUnitOfMeasure>
            
                        <product>
                        <countryOfOrigin>FR</countryOfOrigin>
                        <harmonizationCode>4901.99.0070</harmonizationCode>
                        <description>Book</description>
                        <manufacturerCode></manufacturerCode>
                        <sku></sku>
                        <quantity>2</quantity>
                        <unitValue>14.65</unitValue>
                        <value>29.30</value>
                        <weight>0.5</weight>
                        <productURL>https://www.amazon.com/dp/B01MTNEXLX/</productURL>
                        <FDACode>4-401.11(С)</FDACode>
                        </product>
                        <priorNoticeFilingNumber />
                    </mailItem>
                </shippingApiRequest>
"""