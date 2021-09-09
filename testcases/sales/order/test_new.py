import requests
import json

class TestNewOrder:
    def test_new_order(self):

        url = "http://120.79.172.137:8001/sales/sales/orderagg/api/new"

        payload = json.dumps({
            "clientId": 1427879077875810300,
            "clientName": "广东省_深圳市_沃尔玛（中国）投资有限公司",
            "clientNo": "KHWEMZGTZYXGS0013",
            "createdBy": 1111111111111111200,
            "currency": "人民币",
            "currencyId": 1424926520291360800,
            "paymentMethod": "到付",
            "paymentMethodId": 1425747345462526000,
            "paymentTerms": "货到3天付款",
            "paymentTermsId": 1111111111111111200,
            "rate": 5,
            "remarks": "test",
            "salesContractNo": "AB123456",
            "salesDepartment": "销售",
            "salesDepartmentId": 1425773672739635200,
            "salesOrderDate": "2021-08-27T01:12:23.552Z",
            "salesOrderEntryAggVoList": [
                {
                    "actualUnitPrice": 99.75,
                    "amountExcludingTax": 100,
                    "amountExcludingTaxBc": 105,
                    "avlQtyBu": 100,
                    "avlQtyU": 100,
                    "basicUnit": "kg",
                    "basicUnitId": 1405000805769019400,
                    "createdBy": 1111111111111111200,
                    "createdByName": "小明",
                    "createdOn": "2021-08-27T01:12:23.552Z",
                    "delFlag": 0,
                    "discountAmount": 95,
                    "discountAmountBc": 95,
                    "discountRate": 5,
                    "model": "50g",
                    "orderQtyBu": 200,
                    "orderQtyU": 200,
                    "plannedDeliveryDate": "2021-08-27T01:12:23.552Z",
                    "predictQtyBu": 90,
                    "predictQtyU": 90,
                    "productId": 1407911402512842800,
                    "productName": "芒果半成品",
                    "productNo": "BCNMG001",
                    "remarks": "test",
                    "salesOrderId": 1431161870433124400,
                    "salesPurposeType": "70",
                    "tax": 1,
                    "taxBc": 100,
                    "taxRate": 100,
                    "totalPriceTax": 100,
                    "totalPriceTaxBc": 100,
                    "unit": "5包",
                    "unitId": 1405004270880686000,
                    "unitPrice": 105,
                    "unitPriceExclTax": 100,
                    "updatedBy": 1111111111111111200,
                    "updatedByName": "XXX",
                    "updatedOn": "2021-08-27T01:12:23.552Z"
                }
            ],
            "salesOrderNo": "string",
            "salesPerson": "string",
            "salesPersonId": 0,
            "salesType": "string",
            "salesTypeId": 0,
            "source": "string"
        })
        headers = {
            'USER-SYS-ID': '1',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.json())
        assert response.json().get('success') == True