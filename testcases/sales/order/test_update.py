import requests
import json

class TestUpdateOrder:
    def test_update_order(self):

        url = "http://120.79.172.137:8001/order/sales/order/api/update"

        payload = json.dumps({
            "clientId": 1427879077875810304,
            "clientName": "广东省_深圳市_沃尔玛（中国）投资有限公司",
            "clientNo": "KHWEMZGTZYXGS0013",
            "createdBy": 1111111111111111200,
            "createdByName": "XXX",
            "createdOn": "2021-08-30T02:24:22.698Z",
            "currencyId": 1424926520291360768,
            "id": 1432965475247063040,
            "paymentMethod": "到付",
            "paymentMethodId": 1425747345462525952,
            "paymentTerms": "货到3天付款",
            "paymentTermsId": 1111111111111111200,
            "rate": 5,
            "remarks": "test",
            "salesContractNo": "AB123456",
            "salesDepartment": "销售",
            "salesDepartmentId": 1425773672739635200,
            "salesOrderDate": "2021-08-30T02:24:22.698Z",
            "salesOrderEntryVoList": [
                {
                    "actualUnitPrice": 99.75,
                    "amountExcludingTax": 100,
                    "amountExcludingTaxBc": 105,
                    "avlQtyBu": 100,
                    "avlQtyU": 100,
                    "basicUnit": "kg",
                    "basicUnitId": 1405000805769019392,
                    "createdBy": 1111111111111111200,
                    "createdByName": "XXX",
                    "createdOn": "2021-08-30T02:24:22.698Z",
                    "delFlag": 0,
                    "discountAmount": 95,
                    "discountAmountBc": 95,
                    "discountRate": 5,
                    "id": 1432965475700047872,
                    "model": "50g",
                    "orderQtyBu": 200,
                    "orderQtyU": 200,
                    "plannedDeliveryDate": "2021-08-30T02:24:22.698Z",
                    "predictQtyBu": 90,
                    "predictQtyU": 90,
                    "productId": 1407911402512842752,
                    "productName": "芒果半成品",
                    "productNo": "BCNMG001",
                    "remarks": "test",
                    "salesOrderId": 1431161870433124352,
                    "salesPurposeType": "70",
                    "tax": 1,
                    "taxBc": 100,
                    "taxRate": 100,
                    "totalPriceTax": 100,
                    "totalPriceTaxBc": 100,
                    "unit": "5包",
                    "unitId": 1405004270880686080,
                    "unitPrice": 105,
                    "unitPriceExclTax": 100,
                    "updatedBy": 1111111111111111200,
                    "updatedByName": "XXX",
                    "updatedOn": "2021-08-30T02:24:22.698Z"
            }
        ],
            "salesOrderNo": "string",
            "salesPersonId": 1427444644932747264,
            "salesTypeId": 65,
            "source": "string",
            "updatedBy": 1111111111111111200,
            "updatedByName": "XXX",
            "updatedOn": "2021-08-30T02:24:22.698Z"
        })
        headers = {
            'USER-SYS-ID': '1',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.json())
        assert response.json().get('success') == True