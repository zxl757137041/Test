import os

import pytest
import requests
import json

class TestNewBom:
  def test_new_bom(self):

    url = "http://120.79.172.137:8001/manufacturing/manufacturing/bom/api/new"

    payload = json.dumps({
      "basicUnit": "string",
      "basicUnitId": 1407949900020187100,
      "bomEntryVoList": [
        {
          "basicUnit": "个",
          "basicUnitId": 1407911142453411800,
          "bomType": "物料",
          "createdBy": 1111111111111111200,
          "createdByName": "XXX",
          "createdOn": "2021-07-16T01:17:12.875Z",
          "effectiveDate": "2021-07-16T01:17:12.875Z",
          "loss": 0,
          "materialCode": "FCNMG001",
          "materialId": 1407954776221548500,
          "materialName": "袋子",
          "model": "string",
          "pieceConsumptionBasicUnit": 1,
          "remarks": "string",
          "seq": 0,
          "stopDate": "2021-07-16T01:17:12.875Z",
          "updatedBy": 1111111111111111200,
          "updatedByName": "XXX",
          "updatedOn": "2021-07-16T01:17:12.875Z"
        },
        {
          "basicUnit": "kg",
          "basicUnitId": 1405000805769019400,
          "bomType": "物料",
          "createdBy": 1111111111111111200,
          "createdByName": "XXX",
          "createdOn": "2021-07-16T01:17:12.875Z",
          "effectiveDate": "2021-07-16T01:17:12.875Z",
          "loss": 0,
          "materialCode": "YCNMG001",
          "materialId": 1407905035668422700,
          "materialName": "芒果",
          "model": "string",
          "pieceConsumptionBasicUnit": 100,
          "remarks": "string",
          "seq": 0,
          "stopDate": "2021-07-16T01:17:12.875Z",
          "updatedBy": 1111111111111111200,
          "updatedByName": "XXX",
          "updatedOn": "2021-07-16T01:17:12.875Z"
        }
      ],
      "materialCode": "CCNMG001",
      "materialId": 1407951835813118000,
      "materialName": "亲亲芒",
      "model": "100g*10包*箱",
      "quantityBasicUnit": 1,
      "remarks": "string",
      "status": 0
    })
    headers = {
      'USER-SYS-ID': '1',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())