import requests
import json

class TestUpdatePrice:
    def test_update_price(self):
        url = "http://120.79.172.137:8001/sales/sales/price/api/update"

        payload = json.dumps({
            "actualUnitPrice": 95,
            "basicUnit": "kg",
            "basicUnitId": 1405000805769019400,
            "clientId": 1427879077875810300,
            "clientName": "广东省_深圳市_沃尔玛（中国）投资有限公司",
            "clientNo": "KHWEMZGTZYXGS0013",
            "createdBy": 1111111111111111200,
            "createdByName": "XXX",
            "createdOn": "2021-08-30T09:42:48.053Z",
            "currency": "人民币",
            "currencyId": 1424926520291360800,
            "discountRate": 5,
            "effectiveDate": "2021-08-30T09:42:48.053Z",
            "id": 1432173379531571200,
            "model": "50g",
            "productId": 1407911402512842800,
            "productName": "芒果半成品",
            "productNo": "BCNMG001",
            "remarks": "test",
            "stopDate": "2021-08-30T09:42:48.053Z",
            "taxRate": 5,
            "unit": "5包",
            "unitId": 1405004270880686000,
            "unitPrice": 100,
            "unitPriceExclTax": 95,
            "updatedBy": 1111111111111111200,
            "updatedByName": "XXX",
            "updatedOn": "2021-08-30T09:42:48.053Z",
            "useStatus": 0
        })
        headers = {
            'USER-SYS-ID': '1',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.json())
        assert response.json().get('success') == True

