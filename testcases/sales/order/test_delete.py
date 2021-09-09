import requests
import json

class TestDeleteOrder:
    def test_delete_order(self):

        url = "http://120.79.172.137:8001/order/sales/order/api/deletebyids"

        payload = json.dumps([])
        headers = {
            'USER-SYS-ID': '1',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.json())
        assert response.json().get('success') == True