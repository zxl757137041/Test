import requests
import json

class TestSearchPrice:
    def test_search_price(self):
        url = "http://120.79.172.137:8001/sales/sales/price/api/page/search"

        payload = json.dumps({
            "pageIndex": 1,
            "pageSize": 1,
            "sortField": "id",
            "sortOrder": "desc"
        })
        headers = {
            'USER-SYS-ID': '1',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.json())
        assert response.json().get('success') == True

