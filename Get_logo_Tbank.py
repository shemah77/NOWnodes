import http.client
import json
import os

import requests
import time

API_KEY = os.environ.get(
    "TBANK_API_KEY", None
)  # Put your API key here or in env var

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
            'Authorization': f'Bearer {API_KEY}'
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











