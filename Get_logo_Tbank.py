import http.client
import json
import os
import requests
import time

api_key = 't.szuyzM9-XJdOHb0aV2ZZJO-h5Bm91XISQg7BF0PTdclX1stGYwZZEYLkevshgJ3fDn_bFWJKsincX2rtc-IkqA'

data = {
    "totalAmountShares": {
        "currency": "rub",
        "units": "12173869",
        "nano": 710000000
    },
    "totalAmountBonds": {
        "currency": "rub",
        "units": "0",
        "nano": 0
    },
    "totalAmountEtf": {
        "currency": "rub",
        "units": "3297591",
        "nano": 390000000
    },
    "totalAmountCurrencies": {
        "currency": "rub",
        "units": "488",
        "nano": 230000000
    },
    "totalAmountFutures": {
        "currency": "rub",
        "units": "0",
        "nano": 0
    },
    "expectedYield": {
        "units": "6",
        "nano": 220000000
    },
    "positions": [
        {
            "figi": "TCSB79031078",
            "instrumentType": "share",
            "quantity": {
                "units": "12",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "4511",
                "nano": 10000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "12",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "03333dcb-31b3-4c4f-bfbc-63b52f882073",
            "instrumentUid": "054b5593-5609-40bd-9740-04479351b38c",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US0079031078"
        },
        {
            "figi": "BBG000C5Z1S3",
            "instrumentType": "share",
            "quantity": {
                "units": "19",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "68",
                "nano": 480000000
            },
            "expectedYield": {
                "units": "1558",
                "nano": 150000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "150",
                "nano": 490000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "68",
                "nano": 480000000
            },
            "quantityLots": {
                "units": "19",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "83814c0a-abd3-4b49-907f-2cf8f75c8b3a",
            "instrumentUid": "084be5cb-d603-4ef7-929b-655ee270dd26",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "1558",
                "nano": 150000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "MU"
        },
        {
            "figi": "BBG001VKX1Z1",
            "instrumentType": "share",
            "quantity": {
                "units": "290",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "10",
                "nano": 140000000
            },
            "expectedYield": {
                "units": "-594",
                "nano": -500000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "8",
                "nano": 90000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "10",
                "nano": 140000000
            },
            "quantityLots": {
                "units": "290",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "ea82898f-fd30-4e4f-bf78-51ccf2e5f190",
            "instrumentUid": "0aa8d7c3-ff66-4690-b04e-8f33538e2c19",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-594",
                "nano": -500000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US37827X1000"
        },
        {
            "figi": "DE0005557508",
            "instrumentType": "share",
            "quantity": {
                "units": "156",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "30",
                "nano": 100000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "156",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "f8b2f3de-761a-431a-bcfa-e6616e2503d6",
            "instrumentUid": "0c6ea967-f1d9-4002-9d5b-a69c046f455c",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "20",
                "nano": 280000000
            },
            "ticker": "DE0005557508"
        },
        {
            "figi": "BBG000BNJHS8",
            "instrumentType": "share",
            "quantity": {
                "units": "50",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "38",
                "nano": 740000000
            },
            "expectedYield": {
                "units": "-348",
                "nano": -500000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "31",
                "nano": 770000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "38",
                "nano": 740000000
            },
            "quantityLots": {
                "units": "50",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "9325dd9c-6ce7-4af1-bfbb-edafce386b32",
            "instrumentUid": "12f13bce-bbc6-4bd9-a664-0f1414419718",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-348",
                "nano": -500000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "LUV"
        },
        {
            "figi": "BBG000BT7ZK6",
            "instrumentType": "share",
            "quantity": {
                "units": "155",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "18",
                "nano": 700000000
            },
            "expectedYield": {
                "units": "1634",
                "nano": 230000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "29",
                "nano": 240000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "18",
                "nano": 700000000
            },
            "quantityLots": {
                "units": "155",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "e42d7f51-c356-4c57-97d7-b4d9d4a891ab",
            "instrumentUid": "14eabb09-0942-412f-a7b1-ab649d7906dd",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "1634",
                "nano": 230000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "SONY"
        },
        {
            "figi": "US64110W1027",
            "instrumentType": "share",
            "quantity": {
                "units": "2",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "23",
                "nano": 980000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "2",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "97dafd96-179c-4092-93da-30ff48cd83be",
            "instrumentUid": "17b0cfcd-882b-49c5-a81a-6ae545eb68a4",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US64110W1027"
        },
        {
            "figi": "DE0006599905",
            "instrumentType": "share",
            "quantity": {
                "units": "10",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "107",
                "nano": 300000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "10",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "ba9d6e3a-0a3e-4556-a6ab-d100525d4a7a",
            "instrumentUid": "1e41fce1-ff6d-4d91-8fe1-8ace76c05976",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "-6",
                "nano": 0
            },
            "ticker": "DE0006599905"
        },
        {
            "figi": "TCSB066G1040",
            "instrumentType": "share",
            "quantity": {
                "units": "20",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "4800",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "20",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "4aeb0c83-1f5c-42ec-82ae-ba5e3ad1a065",
            "instrumentUid": "1fb8ce6f-0823-42f6-8e8d-1dc4c12dbfd7",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US67066G1040"
        },
        {
            "figi": "US91912E1055",
            "instrumentType": "share",
            "quantity": {
                "units": "50",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "6",
                "nano": 100000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "50",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "cac73865-96c9-484a-93b0-d2c6f6145ed5",
            "instrumentUid": "20452cd1-2dfe-4100-8ce4-60bc3c347d67",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US91912E1055"
        },
        {
            "figi": "BBG000RTHVK7",
            "instrumentType": "share",
            "quantity": {
                "units": "163",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "3610",
                "nano": 0
            },
            "expectedYield": {
                "units": "-9760",
                "nano": -500000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "3550",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "3610",
                "nano": 0
            },
            "quantityLots": {
                "units": "163",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "86e2defb-6f3e-4556-812f-7c79136c80c2",
            "instrumentUid": "231e5e27-9956-47e7-ad50-6e802e4a92ed",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-9760",
                "nano": -500000000
            },
            "dailyYield": {
                "currency": "rub",
                "units": "7824",
                "nano": 0
            },
            "ticker": "GCHE"
        },
        {
            "figi": "DE0007664039",
            "instrumentType": "share",
            "quantity": {
                "units": "9",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "101",
                "nano": 800000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "9",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "fdf78c0e-a3b2-4c63-9792-80203cd6ed02",
            "instrumentUid": "23529c53-768f-4e7d-b7e3-89cccda69a61",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "-9",
                "nano": 0
            },
            "ticker": "DE0007664039"
        },
        {
            "figi": "TCSB622V1061",
            "instrumentType": "share",
            "quantity": {
                "units": "4",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "140",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "4",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "b94941b4-282d-4eab-8b40-c00e94122b0b",
            "instrumentUid": "242ac7e5-5b2e-40c5-bd31-354cc82381c6",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US68622V1061"
        },
        {
            "figi": "BBG006G2JVL2",
            "instrumentType": "share",
            "quantity": {
                "units": "18",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "247",
                "nano": 790000000
            },
            "expectedYield": {
                "units": "-1661",
                "nano": -770000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "155",
                "nano": 470000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "247",
                "nano": 790000000
            },
            "quantityLots": {
                "units": "18",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "344b79b6-255a-4637-ba18-2e4b8bf5a66a",
            "instrumentUid": "25ec1161-2127-44bc-804d-ea92b6086717",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-1661",
                "nano": -770000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "BABA"
        },
        {
            "figi": "TCS10A1039P6",
            "instrumentType": "etf",
            "quantity": {
                "units": "22000",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "6",
                "nano": 880000000
            },
            "expectedYield": {
                "units": "-45527",
                "nano": -750000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "4",
                "nano": 810000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "6",
                "nano": 880000000
            },
            "quantityLots": {
                "units": "22000",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "9e920ef6-2ca2-465f-955e-202eac77b195",
            "instrumentUid": "2e2a5b8c-2ae3-46a6-90e4-72ab060cb2d8",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-45527",
                "nano": -750000000
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "TGRN"
        },
        {
            "figi": "DE0007236101",
            "instrumentType": "share",
            "quantity": {
                "units": "41",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "228",
                "nano": 850000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "41",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "c0d7ed76-5198-4611-b89e-8c78eee5d915",
            "instrumentUid": "2e52fa43-0b38-4c65-8739-355014bd63e4",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "-8",
                "nano": -200000000
            },
            "ticker": "DE0007236101"
        },
        {
            "figi": "DE0006231004",
            "instrumentType": "share",
            "quantity": {
                "units": "66",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "32",
                "nano": 50000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "66",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "d52586d5-4703-4500-b92d-86eaf88cae93",
            "instrumentUid": "2fee7a9c-3758-4443-9d2e-824ad96d1595",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "8",
                "nano": 580000000
            },
            "ticker": "DE0006231004"
        },
        {
            "figi": "US89151E1091",
            "instrumentType": "share",
            "quantity": {
                "units": "9",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "61",
                "nano": 410000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "9",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "a708cb6b-2ab4-4c67-9634-f7631284e5cd",
            "instrumentUid": "3976d068-3966-4841-b0c9-2dcc1c3c9af5",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US89151E1091"
        },
        {
            "figi": "DE000BAY0017",
            "instrumentType": "share",
            "quantity": {
                "units": "25",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "28",
                "nano": 770000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "25",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "96c08309-57e0-4cf1-bd1b-ac93da18bdba",
            "instrumentUid": "39a89ee3-070f-477a-94c2-7238099c2191",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "6",
                "nano": 750000000
            },
            "ticker": "DE000BAY0017"
        },
        {
            "figi": "DE000A1EWWW0",
            "instrumentType": "share",
            "quantity": {
                "units": "5",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "178",
                "nano": 150000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "5",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "9eeea9cb-bf30-4d58-83e1-4c899419cdbb",
            "instrumentUid": "3d886113-7adc-42be-92cc-cd54c4b4ac23",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "-3",
                "nano": -250000000
            },
            "ticker": "DE000A1EWWW0"
        },
        {
            "figi": "TCSB55121099",
            "instrumentType": "share",
            "quantity": {
                "units": "7",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "2204",
                "nano": 950000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "7",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "b98d3a33-6f33-45f4-9ee7-1f8264442959",
            "instrumentUid": "41cb7462-68d9-4280-805d-9c8ddcf6c2de",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US2855121099"
        },
        {
            "figi": "BBG000BS1YV5",
            "instrumentType": "share",
            "quantity": {
                "units": "7",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "196",
                "nano": 790000000
            },
            "expectedYield": {
                "units": "341",
                "nano": 770000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "245",
                "nano": 610000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "196",
                "nano": 790000000
            },
            "quantityLots": {
                "units": "7",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "065c6c38-c7cd-4bab-bd91-d97762c2564a",
            "instrumentUid": "45743d5b-c2b4-4278-afe2-eec3595e3fc1",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "341",
                "nano": 770000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "TTWO"
        },
        {
            "figi": "BBG0013HRTL0",
            "instrumentType": "currency",
            "quantity": {
                "units": "0",
                "nano": 760000000
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "12",
                "nano": 243100000
            },
            "expectedYield": {
                "units": "0",
                "nano": -260000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "11",
                "nano": 898000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "12",
                "nano": 243000000
            },
            "quantityLots": {
                "units": "0",
                "nano": 760000000
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "176c3dbf-b346-48a6-b20c-daa9d028f031",
            "instrumentUid": "4587ab1d-a9c9-4910-a0d6-86c7b9c42510",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": -260000000
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": -40000000
            },
            "ticker": "CNYRUB_TOM_CETS"
        },
        {
            "figi": "TCSB38721065",
            "instrumentType": "share",
            "quantity": {
                "units": "44",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "600",
                "nano": 120000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "44",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "c4f8c43e-cf0c-4ab2-ad62-7d6ce856b54c",
            "instrumentUid": "45f4e5cc-b663-4985-b448-1dfc63a9e6ce",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US0138721065"
        },
        {
            "figi": "BBG007N0Z367",
            "instrumentType": "share",
            "quantity": {
                "units": "150",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "150",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "f8a4d4f3-92a8-4f09-b77b-127d588ddf04",
            "instrumentUid": "46ae47ee-f409-4776-bf20-43a040b9e7fb",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "AGRO"
        },
        {
            "figi": "BBG00K7T3037",
            "instrumentType": "share",
            "quantity": {
                "units": "8",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "47",
                "nano": 120000000
            },
            "expectedYield": {
                "units": "-181",
                "nano": -360000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "24",
                "nano": 450000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "47",
                "nano": 120000000
            },
            "quantityLots": {
                "units": "8",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "97872c5f-6c5e-4c05-af1c-dc3608b0b882",
            "instrumentUid": "46fef208-a525-4471-85e5-8fe4cee5f8ec",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-181",
                "nano": -360000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "BILI"
        },
        {
            "figi": "BBG000BCCT76",
            "instrumentType": "share",
            "quantity": {
                "units": "7",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "228",
                "nano": 850000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "7",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "960ef143-0e24-4bd5-bcf4-b4c37fdfc13d",
            "instrumentUid": "488189e0-9931-4d8d-8d74-50f4350351ba",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "-1",
                "nano": -400000000
            },
            "ticker": "SIE@DE"
        },
        {
            "figi": "BBG000Q5T9W3",
            "instrumentType": "share",
            "quantity": {
                "units": "47",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "63",
                "nano": 320000000
            },
            "expectedYield": {
                "units": "-1758",
                "nano": -650000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "25",
                "nano": 900000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "63",
                "nano": 320000000
            },
            "quantityLots": {
                "units": "47",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "c083fe98-1752-4b7a-94ee-16586d503fc9",
            "instrumentUid": "4b8e981a-c5b9-45e6-b443-8fbcade389e2",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-1758",
                "nano": -650000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "DQ"
        },
        {
            "figi": "TCSB46871060",
            "instrumentType": "share",
            "quantity": {
                "units": "1",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "3801",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "1",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "80493c2f-3730-429b-b928-d617f41f28f5",
            "instrumentUid": "4f4b7d48-133e-44f2-9fc6-ef44d3996518",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "991",
                "nano": 0
            },
            "ticker": "US2546871060"
        },
        {
            "figi": "US46429B6719",
            "instrumentType": "etf",
            "quantity": {
                "units": "32",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "11",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "32",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "27d925b7-3175-48e4-9298-37af5903dba8",
            "instrumentUid": "4fdcb8b7-47ac-430b-8d8b-6253940895a8",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US46429B6719"
        },
        {
            "figi": "BBG004731489",
            "instrumentType": "share",
            "quantity": {
                "units": "600",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "226",
                "nano": 480000000
            },
            "expectedYield": {
                "units": "-58668",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "128",
                "nano": 700000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "226",
                "nano": 480000000
            },
            "quantityLots": {
                "units": "60",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "8dfc66ef-bd19-4cbc-91b6-22ab581d7dae",
            "instrumentUid": "509edd0c-129c-4ee2-934d-7f6246126da1",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-58668",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "-444",
                "nano": 0
            },
            "ticker": "GMKN"
        },
        {
            "figi": "BBG000BFCS17",
            "instrumentType": "share",
            "quantity": {
                "units": "1",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "204",
                "nano": 110000000
            },
            "expectedYield": {
                "units": "-102",
                "nano": -310000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "101",
                "nano": 800000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "204",
                "nano": 110000000
            },
            "quantityLots": {
                "units": "1",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "e7d51b30-ccd7-4389-b4fb-de269226856f",
            "instrumentUid": "5152007d-e5ab-4c92-ae42-1e89d926d142",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-102",
                "nano": -310000000
            },
            "dailyYield": {
                "currency": "eur",
                "units": "-1",
                "nano": 0
            },
            "ticker": "VOW3@DE"
        },
        {
            "figi": "DE0005552004",
            "instrumentType": "share",
            "quantity": {
                "units": "60",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "38",
                "nano": 520000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "60",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "0e9846ee-8dac-4608-96df-1e7bd107f5c9",
            "instrumentUid": "5532871b-635f-4955-91f0-13ee5a8c5ed1",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "ticker": "DE0005552004"
        },
        {
            "figi": "US2244081046",
            "instrumentType": "share",
            "quantity": {
                "units": "3",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "187",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "3",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "10dcbf88-e1fe-45ea-afe3-1189194f9941",
            "instrumentUid": "61a78dbe-cb19-4f29-b685-cefc89cd1572",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US2244081046"
        },
        {
            "figi": "BBG000BG7GX2",
            "instrumentType": "share",
            "quantity": {
                "units": "28",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "108",
                "nano": 710000000
            },
            "expectedYield": {
                "units": "3138",
                "nano": 520000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "220",
                "nano": 800000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "108",
                "nano": 710000000
            },
            "quantityLots": {
                "units": "28",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "f67dbd41-cab6-49b9-abd9-468818c7b660",
            "instrumentUid": "624f4fa9-fd68-4deb-a4d6-7423d4f1c6b1",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "3138",
                "nano": 520000000
            },
            "dailyYield": {
                "currency": "eur",
                "units": "28",
                "nano": 0
            },
            "ticker": "SAP@DE"
        },
        {
            "figi": "BBG000BH4R78",
            "instrumentType": "share",
            "quantity": {
                "units": "5",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "178",
                "nano": 440000000
            },
            "expectedYield": {
                "units": "-307",
                "nano": -200000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "117",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "178",
                "nano": 440000000
            },
            "quantityLots": {
                "units": "5",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "5ea65eca-5119-4f80-a835-c8729142be3a",
            "instrumentUid": "64aeb159-12e8-48c7-b14a-5211c7301d6c",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-307",
                "nano": -200000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "DIS"
        },
        {
            "figi": "BBG011386VF4",
            "instrumentType": "share",
            "quantity": {
                "units": "1",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "2153",
                "nano": 710000000
            },
            "expectedYield": {
                "units": "-2135",
                "nano": -960000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "17",
                "nano": 750000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "2153",
                "nano": 710000000
            },
            "quantityLots": {
                "units": "1",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "ccfb753a-c44f-478c-947d-caa5d4ebbd37",
            "instrumentUid": "6626d140-b59d-49a2-9d5c-9ec91a8cde0a",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-2135",
                "nano": -960000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "WBD"
        },
        {
            "figi": "TCSB70461096",
            "instrumentType": "share",
            "quantity": {
                "units": "12",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "1315",
                "nano": 110000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "12",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "24de9d70-eaf0-4f81-b323-06bbdaea7271",
            "instrumentUid": "69337ad6-f318-4380-99d6-76e8d8911c52",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US2270461096"
        },
        {
            "figi": "DE0005190003",
            "instrumentType": "share",
            "quantity": {
                "units": "13",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "83",
                "nano": 960000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "13",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "9d251083-2fbc-48c6-bc9f-417d044744cd",
            "instrumentUid": "6a8a328e-7098-4141-a890-b39ee2963ec6",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "-4",
                "nano": -940000000
            },
            "ticker": "DE0005190003"
        },
        {
            "figi": "BBG000BVPV84",
            "instrumentType": "share",
            "quantity": {
                "units": "20",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "169",
                "nano": 940000000
            },
            "expectedYield": {
                "units": "1197",
                "nano": 440000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "229",
                "nano": 810000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "169",
                "nano": 940000000
            },
            "quantityLots": {
                "units": "20",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "c8b5a4af-9ef3-4208-a0e5-e99229f0ef45",
            "instrumentUid": "6de4b6e2-dda9-4c49-9ba8-aa96dc15d33f",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "1197",
                "nano": 440000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "AMZN"
        },
        {
            "figi": "US8740391003",
            "instrumentType": "share",
            "quantity": {
                "units": "12",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "40",
                "nano": 760000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "12",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "aa015f03-a146-4f0c-98fb-b3675c45f918",
            "instrumentUid": "6eaeafcf-90af-4968-a132-4a49126e743b",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US8740391003"
        },
        {
            "figi": "TCSB81191009",
            "instrumentType": "share",
            "quantity": {
                "units": "16",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "2902",
                "nano": 440000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "16",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "e1ec1fdd-a5f4-4b80-9fee-5aaa466aa221",
            "instrumentUid": "6f6354dc-894d-44c5-b3ab-062f1fba4463",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US8581191009"
        },
        {
            "figi": "BBG000C0G1D1",
            "instrumentType": "share",
            "quantity": {
                "units": "17",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "57",
                "nano": 120000000
            },
            "expectedYield": {
                "units": "-553",
                "nano": -350000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "24",
                "nano": 570000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "57",
                "nano": 120000000
            },
            "quantityLots": {
                "units": "17",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "cb6b0d66-181b-4462-ade8-486754b3afe7",
            "instrumentUid": "70a02b59-62ba-42b0-b528-a56907cb912c",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-553",
                "nano": -350000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "INTC"
        },
        {
            "figi": "US0567521085",
            "instrumentType": "share",
            "quantity": {
                "units": "3",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "33",
                "nano": 10000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "3",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "91237ed4-cbf5-47df-846d-3030cc22b51b",
            "instrumentUid": "73ae8eec-16ac-4493-b289-09b5b362572b",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US0567521085"
        },
        {
            "figi": "BBG000BND699",
            "instrumentType": "share",
            "quantity": {
                "units": "7",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "211",
                "nano": 970000000
            },
            "expectedYield": {
                "units": "77",
                "nano": 210000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "223",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "211",
                "nano": 970000000
            },
            "quantityLots": {
                "units": "7",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "44027a66-54b4-4153-8439-b170e7fbf444",
            "instrumentUid": "75bc00c6-f872-48af-ac8c-fb8fd6af4762",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "77",
                "nano": 210000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "NXPI"
        },
        {
            "figi": "TCSB106L1098",
            "instrumentType": "share",
            "quantity": {
                "units": "3",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "4005",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "3",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "b1856bac-d859-4f4c-bb37-4b932923669e",
            "instrumentUid": "77a8a869-6127-4413-ae26-55530fdb7a69",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US94106L1098"
        },
        {
            "figi": "BBG00KMXFK61",
            "instrumentType": "etf",
            "quantity": {
                "units": "194",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "1699",
                "nano": 500000000
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "1699",
                "nano": 500000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "1699",
                "nano": 500000000
            },
            "quantityLots": {
                "units": "194",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "05f59199-0398-43d3-ab59-d1f1ec9cab45",
            "instrumentUid": "77e0e29f-93bd-436a-95fb-b4a1b606ea3a",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "RUSE"
        },
        {
            "figi": "US4642872000",
            "instrumentType": "etf",
            "quantity": {
                "units": "63",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "150",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "63",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "4afaf681-a213-4e79-8417-d1739f1f3a54",
            "instrumentUid": "7931b397-c56c-4bb8-9c9e-3f3f3288e9bc",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US4642872000"
        },
        {
            "figi": "DE0005313704",
            "instrumentType": "share",
            "quantity": {
                "units": "27",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "42",
                "nano": 600000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "27",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "7df0d21c-f8d1-4a4c-8868-fa9d49799bc8",
            "instrumentUid": "79a87795-b30e-46f2-860b-5ec9c6f15621",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "2",
                "nano": 700000000
            },
            "ticker": "DE0005313704"
        },
        {
            "figi": "TCS228071082",
            "instrumentType": "share",
            "quantity": {
                "units": "30",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "115",
                "nano": 510000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "30",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "570138ab-0e01-4cd8-87c9-63fd6bb051e9",
            "instrumentUid": "79cc549d-a522-4f38-96ea-1ec4ef9eb80d",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "LRCX"
        },
        {
            "figi": "TCSB332U1016",
            "instrumentType": "share",
            "quantity": {
                "units": "11",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "1000",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "11",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "540fe90f-5abc-4df2-ba66-7a3b4a2e0a47",
            "instrumentUid": "7a34af6b-5c5c-4f19-9ebc-3293720ac2dd",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US91332U1016"
        },
        {
            "figi": "BBG000BD8ZK0",
            "instrumentType": "share",
            "quantity": {
                "units": "13",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "101",
                "nano": 600000000
            },
            "expectedYield": {
                "units": "2044",
                "nano": 880000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "258",
                "nano": 900000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "101",
                "nano": 600000000
            },
            "quantityLots": {
                "units": "13",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "e65c2105-85f1-4739-9d1e-5650f986edc3",
            "instrumentUid": "7d24ab0a-e707-4a9e-8d78-6ee07e164881",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "2044",
                "nano": 880000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "TSM"
        },
        {
            "figi": "BBG000BBXB74",
            "instrumentType": "share",
            "quantity": {
                "units": "6",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "60",
                "nano": 260000000
            },
            "expectedYield": {
                "units": "142",
                "nano": 200000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "83",
                "nano": 960000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "60",
                "nano": 260000000
            },
            "quantityLots": {
                "units": "6",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "dc6e0703-11ee-4220-96eb-52bebac6f950",
            "instrumentUid": "81c03456-b40b-4da0-a68a-97bbdfffaeca",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "142",
                "nano": 200000000
            },
            "dailyYield": {
                "currency": "eur",
                "units": "-2",
                "nano": -280000000
            },
            "ticker": "BMW@DE"
        },
        {
            "figi": "BBG000HS77T5",
            "instrumentType": "share",
            "quantity": {
                "units": "25",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "58",
                "nano": 330000000
            },
            "expectedYield": {
                "units": "-357",
                "nano": -250000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "44",
                "nano": 40000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "58",
                "nano": 330000000
            },
            "quantityLots": {
                "units": "25",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "57d6a4fc-d135-4c17-abb2-3f05ad9357e7",
            "instrumentUid": "86fd3b79-9377-47c9-a1ce-6dcd0c843569",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-357",
                "nano": -250000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "VZ"
        },
        {
            "figi": "BBG008NMBXN8",
            "instrumentType": "share",
            "quantity": {
                "units": "10",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "49",
                "nano": 390000000
            },
            "expectedYield": {
                "units": "687",
                "nano": 500000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "118",
                "nano": 140000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "49",
                "nano": 390000000
            },
            "quantityLots": {
                "units": "10",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "1b914524-c134-4771-a384-42892f7f4850",
            "instrumentUid": "873174ca-e522-456a-a7ab-e5003561b48c",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "687",
                "nano": 500000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "HOOD"
        },
        {
            "figi": "DE0006048432",
            "instrumentType": "share",
            "quantity": {
                "units": "40",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "74",
                "nano": 120000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "40",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "34df3752-73eb-4a67-b984-4c832bb7c5e5",
            "instrumentUid": "878f1978-f173-425a-9bcf-6bd4cc141279",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "ticker": "DE0006048432"
        },
        {
            "figi": "NL0009538784",
            "instrumentType": "share",
            "quantity": {
                "units": "1",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "223",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "1",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "b3980773-d070-4a8c-aeda-00519be200db",
            "instrumentUid": "881feade-e91d-4671-853a-df09c6b7a1ff",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "NL0009538784"
        },
        {
            "figi": "US2244411052",
            "instrumentType": "share",
            "quantity": {
                "units": "3",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "61",
                "nano": 930000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "3",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "58089058-334f-418a-b39a-8fabd8cab454",
            "instrumentUid": "8ad6b5e8-11f8-45b9-8628-a9bb259e31f7",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US2244411052"
        },
        {
            "figi": "TCSB40541094",
            "instrumentType": "share",
            "quantity": {
                "units": "1",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "3600",
                "nano": 210000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "1",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "70a617f1-b391-4ebe-8d09-d55a7df6da8e",
            "instrumentUid": "8ba4041d-a348-48c5-9800-de55e46a9b5a",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US8740541094"
        },
        {
            "figi": "TCSB21891057",
            "instrumentType": "share",
            "quantity": {
                "units": "1",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "1000",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "1",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "43f6250c-89d3-453e-83e1-7646d143f369",
            "instrumentUid": "8bafec3f-77e7-4734-be4c-c32fda63b4e7",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US6821891057"
        },
        {
            "figi": "TCSB52691001",
            "instrumentType": "share",
            "quantity": {
                "units": "30",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "1221",
                "nano": 990000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "30",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "9d2e8437-513e-4a73-ab7f-025252895e03",
            "instrumentUid": "93fee89b-23a9-4c42-9730-366edc6cbe0e",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US1252691001"
        },
        {
            "figi": "BBG004730RP0",
            "instrumentType": "share",
            "quantity": {
                "units": "3960",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "258",
                "nano": 0
            },
            "expectedYield": {
                "units": "-508549",
                "nano": -780000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "129",
                "nano": 580000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "258",
                "nano": 0
            },
            "quantityLots": {
                "units": "396",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "4f9d0c81-cdf9-4735-8295-bacbfa3b8a51",
            "instrumentUid": "962e2a95-02a9-4171-abd7-aa198dbe643a",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-508549",
                "nano": -780000000
            },
            "dailyYield": {
                "currency": "rub",
                "units": "-1742",
                "nano": -400000000
            },
            "ticker": "GAZP"
        },
        {
            "figi": "BBG000TY1CD1",
            "instrumentType": "share",
            "quantity": {
                "units": "967",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "453",
                "nano": 0
            },
            "expectedYield": {
                "units": "343831",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "433",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "77",
                "nano": 400000000
            },
            "quantityLots": {
                "units": "967",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "7e12ee80-9a45-4011-878f-593d810e9277",
            "instrumentUid": "974077c4-d893-4058-9314-8f1b64a444b8",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "343831",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "-2320",
                "nano": -800000000
            },
            "ticker": "BELU"
        },
        {
            "figi": "TCSB206R1023",
            "instrumentType": "share",
            "quantity": {
                "units": "53",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "800",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "53",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "f51bc9e3-d384-4846-af2b-2a749306b9c2",
            "instrumentUid": "998ee7af-054e-442c-bdf9-140f1414c580",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US00206R1023"
        },
        {
            "figi": "BBG000BPH459",
            "instrumentType": "share",
            "quantity": {
                "units": "21",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "301",
                "nano": 990000000
            },
            "expectedYield": {
                "units": "4368",
                "nano": 280000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "510",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "301",
                "nano": 990000000
            },
            "quantityLots": {
                "units": "21",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "14ed5263-ac0f-49e8-b6bd-b9abc15699a0",
            "instrumentUid": "99cfdf6a-8b64-44b1-b38e-c831f77d552d",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "4368",
                "nano": 280000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "MSFT"
        },
        {
            "figi": "TCS90A0JQUZ6",
            "instrumentType": "share",
            "quantity": {
                "units": "1052",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "154",
                "nano": 540000000
            },
            "expectedYield": {
                "units": "-25269",
                "nano": -40000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "130",
                "nano": 520000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "154",
                "nano": 540000000
            },
            "quantityLots": {
                "units": "1052",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "adc78cdb-d662-45cd-85d6-f5e605966b9e",
            "instrumentUid": "9b9a584e-448f-40da-9ba8-353b44ad697a",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-25269",
                "nano": -40000000
            },
            "dailyYield": {
                "currency": "rub",
                "units": "1283",
                "nano": 440000000
            },
            "ticker": "RAGR"
        },
        {
            "figi": "BBG000C8L273",
            "instrumentType": "share",
            "quantity": {
                "units": "23",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "30",
                "nano": 910000000
            },
            "expectedYield": {
                "units": "26",
                "nano": 200000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "32",
                "nano": 50000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "30",
                "nano": 910000000
            },
            "quantityLots": {
                "units": "23",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "de390b98-43e6-4dd1-b2bf-1ef37412f891",
            "instrumentUid": "a3f4af1c-b487-4a11-a099-170bd5ab2266",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "26",
                "nano": 200000000
            },
            "dailyYield": {
                "currency": "eur",
                "units": "2",
                "nano": 990000000
            },
            "ticker": "IFX@DE"
        },
        {
            "figi": "TCS5985W2044",
            "instrumentType": "share",
            "quantity": {
                "units": "25",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "118",
                "nano": 10000000
            },
            "expectedYield": {
                "units": "-2749",
                "nano": -500000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "8",
                "nano": 30000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "118",
                "nano": 10000000
            },
            "quantityLots": {
                "units": "25",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "80f82536-4357-4c76-a5b9-b115b972b39b",
            "instrumentUid": "a62f6a47-eb46-4348-8e38-046f42172267",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-2749",
                "nano": -500000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US25985W2044"
        },
        {
            "figi": "USD800UTSTOM",
            "instrumentType": "currency",
            "quantity": {
                "units": "5",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "91",
                "nano": 350000000
            },
            "expectedYield": {
                "units": "-27",
                "nano": -730000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "85",
                "nano": 660000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "91",
                "nano": 210000000
            },
            "quantityLots": {
                "units": "5",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "6e97aa9b-50b6-4738-bce7-17313f2b2cc2",
            "instrumentUid": "a72dafc0-7f40-48ce-9dc8-770cf4222a24",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-27",
                "nano": -730000000
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "USD000UTSTOM"
        },
        {
            "figi": "TCSB81021055",
            "instrumentType": "share",
            "quantity": {
                "units": "12",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "1008",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "12",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "cf85098f-3a96-4677-9f23-ec5521fea6cf",
            "instrumentUid": "a8af6f55-3beb-4a97-b188-0d6d7857b560",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US9581021055"
        },
        {
            "figi": "US30303M1027",
            "instrumentType": "share",
            "quantity": {
                "units": "1",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "751",
                "nano": 710000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "1",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "7aa52132-86a4-4cfb-a51b-3e9c585b8132",
            "instrumentUid": "ab22403a-83ad-4892-911a-20d9d8cf6adc",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US30303M1027"
        },
        {
            "figi": "BBG00RPRPX12",
            "instrumentType": "etf",
            "quantity": {
                "units": "1119439",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "1",
                "nano": 619900000
            },
            "expectedYield": {
                "units": "157505",
                "nano": 70000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "1",
                "nano": 796800000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "1",
                "nano": 656100000
            },
            "quantityLots": {
                "units": "1119439",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "eee36ccf-5f28-4419-9c29-c6465f39581a",
            "instrumentUid": "ade12bc5-07d9-44fe-b27a-1543e05bacfd",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "157505",
                "nano": 70000000
            },
            "dailyYield": {
                "currency": "rub",
                "units": "2686",
                "nano": 650000000
            },
            "ticker": "LQDT"
        },
        {
            "figi": "TCS0BD3QFB18",
            "instrumentType": "etf",
            "quantity": {
                "units": "25",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "2745",
                "nano": 0
            },
            "expectedYield": {
                "units": "-57650",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "439",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "2745",
                "nano": 0
            },
            "quantityLots": {
                "units": "25",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "93d94da5-ee5d-44f9-964d-42d580feda36",
            "instrumentUid": "af6fd8d3-da6a-4b3b-baff-33f5f76938f0",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-57650",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "-375",
                "nano": 0
            },
            "ticker": "IE00BD3QFB18"
        },
        {
            "figi": "BBG000QXWHD1",
            "instrumentType": "share",
            "quantity": {
                "units": "8",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "186",
                "nano": 440000000
            },
            "expectedYield": {
                "units": "-595",
                "nano": -460000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "112",
                "nano": 10000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "186",
                "nano": 440000000
            },
            "quantityLots": {
                "units": "8",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "53fdfd2a-8b7d-4154-9717-e6405a54b9a3",
            "instrumentUid": "b09c2b51-9402-4ad0-8b18-1db0eb8a86bb",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-595",
                "nano": -460000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "BIDU"
        },
        {
            "figi": "BBG0056JW5G6",
            "instrumentType": "share",
            "quantity": {
                "units": "7",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "106",
                "nano": 310000000
            },
            "expectedYield": {
                "units": "-440",
                "nano": -90000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "43",
                "nano": 440000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "106",
                "nano": 310000000
            },
            "quantityLots": {
                "units": "7",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "38a5c91d-5a54-4648-b3dd-83bd97cb6b97",
            "instrumentUid": "b19d6749-4557-49ff-9f55-621f626e5bcb",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-440",
                "nano": -90000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "U"
        },
        {
            "figi": "BBG0013HJJ31",
            "instrumentType": "currency",
            "quantity": {
                "units": "0",
                "nano": 510000000
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "59",
                "nano": 485000000
            },
            "expectedYield": {
                "units": "20",
                "nano": 530000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "99",
                "nano": 736700000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "59",
                "nano": 485000000
            },
            "quantityLots": {
                "units": "0",
                "nano": 510000000
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "2415fb51-2ebe-4669-8ea4-9ba09e765366",
            "instrumentUid": "b1c06e5e-f5d4-4ff5-8cb3-dcacccd933da",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "20",
                "nano": 530000000
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "EUR_RUB__TOM_CETS"
        },
        {
            "figi": "IE00BTN1Y115",
            "instrumentType": "share",
            "quantity": {
                "units": "20",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "93",
                "nano": 990000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "20",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "21058b32-36e0-434c-9ebc-cf07ed02efef",
            "instrumentUid": "b4f8fe7b-40a1-45f0-a07b-5bdfce64f8a8",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "IE00BTN1Y115"
        },
        {
            "figi": "TCS0004C2008",
            "instrumentType": "share",
            "quantity": {
                "units": "4",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "84",
                "nano": 500000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "4",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "52ed04f9-3336-4228-987d-5474288679bc",
            "instrumentUid": "b63ac024-a4a2-4783-b2ba-5a3c5386e815",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "1",
                "nano": 160000000
            },
            "ticker": "US80004C2008"
        },
        {
            "figi": "BBG000HJTMS9",
            "instrumentType": "share",
            "quantity": {
                "units": "1",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "16",
                "nano": 580000000
            },
            "expectedYield": {
                "units": "13",
                "nano": 520000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "30",
                "nano": 100000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "16",
                "nano": 580000000
            },
            "quantityLots": {
                "units": "1",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "bb7640fe-d562-4269-b749-4b7d13eb71cf",
            "instrumentUid": "baf77b85-893a-4260-bf90-14d1ea7328b1",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "13",
                "nano": 520000000
            },
            "dailyYield": {
                "currency": "eur",
                "units": "0",
                "nano": 130000000
            },
            "ticker": "DTE@DE"
        },
        {
            "figi": "TCSB44231041",
            "instrumentType": "share",
            "quantity": {
                "units": "11",
                "nano": 820000000
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "116",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "11",
                "nano": 820000000
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "15fcce40-e053-46ea-9d8d-2190d4f450f5",
            "instrumentUid": "bb7e1347-a8cd-4d04-b35b-16de55481427",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US9344231041"
        },
        {
            "figi": "TCSB91231015",
            "instrumentType": "share",
            "quantity": {
                "units": "1",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "6100",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "1",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "3439dd8a-8499-4124-ab47-970ecf71a2e4",
            "instrumentUid": "bbae5d9e-9838-4c8a-967f-1b4d561beeb0",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US1491231015"
        },
        {
            "figi": "BBG0047315Y7",
            "instrumentType": "share",
            "quantity": {
                "units": "800",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "261",
                "nano": 600000000
            },
            "expectedYield": {
                "units": "36774",
                "nano": 100000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "307",
                "nano": 570000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "261",
                "nano": 600000000
            },
            "quantityLots": {
                "units": "800",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "9cf9718d-50df-4326-a205-cf306933607e",
            "instrumentUid": "c190ff1f-1447-4227-b543-316332699ca5",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "36774",
                "nano": 100000000
            },
            "dailyYield": {
                "currency": "rub",
                "units": "136",
                "nano": 0
            },
            "ticker": "SBERP"
        },
        {
            "figi": "TCSB28241000",
            "instrumentType": "share",
            "quantity": {
                "units": "5",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "1201",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "5",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "f3ae8e34-3335-40db-8f1e-1a5264a3722b",
            "instrumentUid": "c87098c5-1763-4dc1-82cb-8511ba826028",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "199",
                "nano": 750000000
            },
            "ticker": "US0028241000"
        },
        {
            "figi": "TCSB532F1003",
            "instrumentType": "share",
            "quantity": {
                "units": "14",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "8000",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "14",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "5b0b66b7-fdf0-483b-bf93-e310f60c437e",
            "instrumentUid": "cbc7fc45-2fce-4589-b154-e6ed03821974",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US92532F1003"
        },
        {
            "figi": "BBG00JXPFBN0",
            "instrumentType": "share",
            "quantity": {
                "units": "5",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "5",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "561ec26b-608e-4c83-8c9d-ab5f3b03e235",
            "instrumentUid": "cc68221f-cc21-42a4-a52f-d819bfe4d4c0",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "FIVE"
        },
        {
            "figi": "US01609W1027",
            "instrumentType": "share",
            "quantity": {
                "units": "7",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "20",
                "nano": 20000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "7",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "e1cc1092-0cac-4097-bdb3-09e9ff7104f0",
            "instrumentUid": "cd5ef90c-8ee0-417c-b01a-b71092e9ec94",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US01609W1027"
        },
        {
            "figi": "BBG000BJPDZ1",
            "instrumentType": "share",
            "quantity": {
                "units": "5",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "342",
                "nano": 800000000
            },
            "expectedYield": {
                "units": "561",
                "nano": 20000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "455",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "342",
                "nano": 800000000
            },
            "quantityLots": {
                "units": "5",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "b6569d8d-5d60-4001-990b-d94b985fe6e6",
            "instrumentUid": "cd769ec0-5d9d-4092-a387-7d73fa6fa705",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "561",
                "nano": 20000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "ISRG"
        },
        {
            "figi": "US0900401060",
            "instrumentType": "share",
            "quantity": {
                "units": "2",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "3",
                "nano": 940000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "2",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "9f38ab9e-11bf-4970-af3e-c0dbf150282a",
            "instrumentUid": "d31556ac-3178-40bd-9988-656b4ac96b24",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US0900401060"
        },
        {
            "figi": "TCSB49181045",
            "instrumentType": "share",
            "quantity": {
                "units": "6",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "15000",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "6",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "783c780f-6e6d-4e18-b546-b6033f961f2b",
            "instrumentUid": "dd3be5f6-9e3b-4776-b98b-4c959624420a",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US5949181045"
        },
        {
            "figi": "BBG000BYLJ52",
            "instrumentType": "share",
            "quantity": {
                "units": "118",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "25",
                "nano": 990000000
            },
            "expectedYield": {
                "units": "447",
                "nano": 810000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "29",
                "nano": 780000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "25",
                "nano": 990000000
            },
            "quantityLots": {
                "units": "118",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "04c17e0f-9467-4c18-b7bd-e34cb16f8850",
            "instrumentUid": "e0d4b00b-ee38-4b8a-acf5-64818459bd2f",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "447",
                "nano": 810000000
            },
            "dailyYield": {
                "currency": "eur",
                "units": "9",
                "nano": 440000000
            },
            "ticker": "LU1598757687"
        },
        {
            "figi": "DE000ENAG999",
            "instrumentType": "share",
            "quantity": {
                "units": "200",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "eur",
                "units": "15",
                "nano": 520000000
            },
            "averagePositionPriceFifo": {
                "currency": "eur",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "200",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "f02f3935-4ddb-4461-a374-2ba30c937c03",
            "instrumentUid": "e145dfe2-93dc-4413-aad4-fbbe782b6ed9",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "eur",
                "units": "42",
                "nano": 0
            },
            "ticker": "DE000ENAG999"
        },
        {
            "figi": "TCSB75251036",
            "instrumentType": "share",
            "quantity": {
                "units": "12",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "2800",
                "nano": 100000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "12",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "6ea4bf42-8637-4d5a-b5a2-88cac0e5326d",
            "instrumentUid": "e3b4941a-85ec-43e1-8ca4-efb12f884116",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US7475251036"
        },
        {
            "figi": "BBG004730N88",
            "instrumentType": "share",
            "quantity": {
                "units": "820",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "257",
                "nano": 460000000
            },
            "expectedYield": {
                "units": "41310",
                "nano": 400000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "307",
                "nano": 840000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "257",
                "nano": 460000000
            },
            "quantityLots": {
                "units": "820",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "41eb2102-5333-4713-bf15-72b204c4bf7b",
            "instrumentUid": "e6123145-9665-43e0-8413-cd61b8aa9b13",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "41310",
                "nano": 400000000
            },
            "dailyYield": {
                "currency": "rub",
                "units": "598",
                "nano": 600000000
            },
            "ticker": "SBER"
        },
        {
            "figi": "TCSB01351017",
            "instrumentType": "share",
            "quantity": {
                "units": "5",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "8600",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "5",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "6e2edb44-53e6-4443-901c-10582d3b9839",
            "instrumentUid": "ed9e39d9-eb14-4827-b925-244ae4cbd719",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US5801351017"
        },
        {
            "figi": "BBG00ZGF7771",
            "instrumentType": "share",
            "quantity": {
                "units": "3",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "275",
                "nano": 280000000
            },
            "expectedYield": {
                "units": "150",
                "nano": 670000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "325",
                "nano": 500000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "275",
                "nano": 280000000
            },
            "quantityLots": {
                "units": "3",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "e48a9b85-1747-4298-bc39-2d7518e03468",
            "instrumentUid": "ef07da8c-00c3-43cb-b8dd-d7c5d5585ec1",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "150",
                "nano": 670000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "COIN"
        },
        {
            "figi": "US50202M1027",
            "instrumentType": "share",
            "quantity": {
                "units": "40",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "8",
                "nano": 800000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "40",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "1e41aa65-dac5-41fa-9daa-87456afc20bb",
            "instrumentUid": "f11315d8-55d7-4cbc-a5f5-96645752c4ff",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US50202M1027"
        },
        {
            "figi": "TCS9273V1008",
            "instrumentType": "share",
            "quantity": {
                "units": "3",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "8",
                "nano": 290000000
            },
            "expectedYield": {
                "units": "27",
                "nano": 600000000
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "17",
                "nano": 490000000
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "8",
                "nano": 290000000
            },
            "quantityLots": {
                "units": "3",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "2b73434e-72fd-496a-87a8-852fd67b511c",
            "instrumentUid": "f194e22a-dfba-44ce-9b3c-fdc4f95372e9",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "27",
                "nano": 600000000
            },
            "dailyYield": {
                "currency": "usd",
                "units": "0",
                "nano": 0
            },
            "ticker": "US29273V1008"
        },
        {
            "figi": "BBG000BSD055",
            "instrumentType": "share",
            "quantity": {
                "units": "2",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "usd",
                "units": "1895",
                "nano": 0
            },
            "expectedYield": {
                "units": "-1068",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "usd",
                "units": "1361",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "usd",
                "units": "1895",
                "nano": 0
            },
            "quantityLots": {
                "units": "2",
                "nano": 0
            },
            "blocked": "false",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "93f50ca6-c39b-4ccb-917f-1fd89d322a83",
            "instrumentUid": "f3b08286-4501-437b-aa79-650e87671e47",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "-1068",
                "nano": 0
            },
            "dailyYield": {
                "currency": "usd",
                "units": "28",
                "nano": 0
            },
            "ticker": "SMSN"
        },
        {
            "figi": "TCSB05051046",
            "instrumentType": "share",
            "quantity": {
                "units": "1",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "1410",
                "nano": 100000000
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "1",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "c2f68cc1-74d1-41a1-98af-1a279c6fce3b",
            "instrumentUid": "f40bc75a-cdc8-4792-87a9-20baf9e84189",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US0605051046"
        },
        {
            "figi": "TCSB73617023",
            "instrumentType": "share",
            "quantity": {
                "units": "30",
                "nano": 0
            },
            "averagePositionPrice": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "expectedYield": {
                "units": "0",
                "nano": 0
            },
            "averagePositionPricePt": {
                "units": "0",
                "nano": 0
            },
            "currentPrice": {
                "currency": "rub",
                "units": "1550",
                "nano": 0
            },
            "averagePositionPriceFifo": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "quantityLots": {
                "units": "30",
                "nano": 0
            },
            "blocked": "true",
            "blockedLots": {
                "units": "0",
                "nano": 0
            },
            "positionUid": "5ce32cfe-e7b9-4424-8559-8fb2dd76f5b0",
            "instrumentUid": "f7159616-4fcb-428c-9478-7c4f0a720e0f",
            "varMargin": {
                "currency": "",
                "units": "0",
                "nano": 0
            },
            "expectedYieldFifo": {
                "units": "0",
                "nano": 0
            },
            "dailyYield": {
                "currency": "rub",
                "units": "0",
                "nano": 0
            },
            "ticker": "US2473617023"
        }
    ],
    "accountId": "2033128386",
    "totalAmountOptions": {
        "currency": "rub",
        "units": "0",
        "nano": 0
    },
    "totalAmountSp": {
        "currency": "rub",
        "units": "0",
        "nano": 0
    },
    "totalAmountPortfolio": {
        "currency": "rub",
        "units": "15471949",
        "nano": 330000000
    },
    "virtualPositions": [],
    "dailyYield": {
        "currency": "rub",
        "units": "19792",
        "nano": 860000000
    },
    "dailyYieldRelative": {
        "units": "0",
        "nano": 130000000
    }
}

uids = [pos["instrumentUid"] for pos in data["positions"] if "instrumentUid" in pos]
print(uids)

def get_isin (uid: str) -> str:
    conn = http.client.HTTPSConnection("invest-public-api.tbank.ru")
    payload = json.dumps({
            "idType": "INSTRUMENT_ID_TYPE_UID",
            "classCode": "string",
            "id": uid
        })
    headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer t.szuyzM9-XJdOHb0aV2ZZJO-h5Bm91XISQg7BF0PTdclX1stGYwZZEYLkevshgJ3fDn_bFWJKsincX2rtc-IkqA'
         }
    conn.request(
            "POST",
            "/rest/tinkoff.public.invest.api.contract.v1.InstrumentsService/GetInstrumentBy",
            payload,
            headers
        )
    res = conn.getresponse()
    print ('Response code: ', res.status)
    data = res.read()
    data_json = json.loads(data.decode("utf-8"))
    print (data_json["instrument"]["isin"])
    isin = data_json["instrument"]["isin"]
    time.sleep(1)
    return isin


def download_company_logo(logo_name: str, size: int = 160, save_path: str = None) -> bytes:
    """
    Скачать логотип компании по его имени (logo_name) и размеру.

    Args:
        logo_name (str): Имя логотипа, обычно FIGI-идентификатор, например "US87238U20333".
        size (int): Размер логотипа в пикселях (одно из 160, 320 или 640). По умолчанию 160.
        save_path (str, optional): Путь для сохранения файла. Если не указан, функция возвращает байты файла.

    Returns:
        bytes: Содержимое PNG-файла логотипа.
    """
    if size not in (160, 320, 640):
        raise ValueError("Неверный размер логотипа. Допустимые размеры: 160, 320, 640")

    try:
        url = f"https://invest-brands.cdn-tinkoff.ru/{logo_name}x{size}.png"

        response = requests.get(url, timeout=10)

        response.raise_for_status()  # выбрасывает исключение при ошибке загрузки

    except requests.exceptions.HTTPError as e:
        print(f"❌ Ошибка HTTP {response.status_code} для {url}: {e}")
        return None, url
    except:
        raise ValueError("Неверный ответ сервера")
    content = response.content
    print(url)

    if not content or len(content) < 50:  # 50 байт как минимальный порог
        print(f"⚠ Пустой или битый файл для {logo_name}, не сохраняем.")
        return None, url

    if save_path:
        with open(save_path, "wb") as f:
            f.write(content)

    return content

if __name__ == "__main__":
    uids = [pos["instrumentUid"] for pos in data["positions"] if "instrumentUid" in pos]
    print(uids)
    for uid in uids:
        isin = get_isin(uid)
        folder = "logo"
        filename = f"{isin}.png"
        save_path = os.path.join(folder, filename)
        print(isin)
        logo_data = download_company_logo(isin, size=320, save_path=save_path)











