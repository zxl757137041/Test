import requests
import json

class TestDeletePrice:
    def test_delete_price(self):
        url = "http://120.79.172.137:8001/sales/sales/price/api/deletebyids"

        payload = json.dumps([])
        headers = {
            'USER-SYS-ID': '1',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.json())
        assert response.json().get('success') == True

