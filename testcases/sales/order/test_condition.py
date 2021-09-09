import requests
import json

class TestConditionOrder:
  def test_condition_order(self):
    url = "http://120.79.172.137:8001/sales/sales/orderagg/api/page/condition"

    payload = json.dumps({
      "page": {
        "pageIndex": 1,
        "pageSize": 1
      }
    })
    headers = {
      'USER-SYS-ID': '1',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
    assert response.json().get('success') == True
