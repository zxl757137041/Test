import requests
import json
from db import result
a = result.get('ID')
b = result.get('ACT_PROCESS_ID')


class TestApproveOrder:
    def test_approve_order(self):
        url = "http://120.79.172.137:8001/sales/sales/orderagg/api/approve"

        payload = json.dumps({
            "comment": "同意",
            "objId": a,
            "processId": b,
            "result": "1",
            "title": "1",
            "type": 1,
            "userId": 1111111111111111200
        })
        headers = {
            'USER-SYS-ID': '1111111111111111200',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.json())
        print(a,b)
        assert response.json().get('success') == True


