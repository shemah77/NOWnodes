import yfinance as yf
import pprint
from urllib.parse import urlparse


def norm_domain_from_website(website: str) -> str:
    """Извлечь домен из URL/строки."""
    website = website.strip()
    if not website:
        raise ValueError("Пустой website.")
    if not website.startswith(("http://", "https://")):
        website = "https://" + website
    u = urlparse(website)
    host = (u.netloc or u.path).split("/")[0]
    if not host:
        raise ValueError(f"Не удалось извлечь домен из '{website}'")
    return host


import requests
import os


def fetch_clearbit_logo(domain: str, output: str = None, size: int = 128, try_www: bool = True,
                        timeout: int = 10) -> str:
    """
    Скачивает логотип компании по домену через Clearbit Logo API.

    :param domain: Домен компании (например, "apple.com" или "microsoft.com")
    :param output: Имя файла для сохранения (по умолчанию <domain>.png)
    :param size: Размер иконки (например 64, 128, 256, 512)
    :param try_www: Пробовать ли домен с префиксом www, если не найден
    :param timeout: Таймаут HTTP-запроса
    :return: Путь к сохранённому файлу
    """

    def _request(d: str) -> requests.Response:
        url = f"https://logo.clearbit.com/{d}"
        return requests.get(url, params={"size": str(size)}, timeout=timeout)

    resp = _request(domain)
    if not (resp.status_code == 200 and resp.content):
        if try_www and not domain.startswith("www."):
            resp = _request("www." + domain)

    if resp.status_code != 200 or not resp.content:
        raise ValueError(f"Clearbit не вернул логотип для {domain} (HTTP {resp.status_code})")

    # имя файла
    if output is None:
        base = domain.replace("www.", "").replace("/", "_")
        output = f"{base}_{size}.png"

    with open(output, "wb") as f:
        f.write(resp.content)

    return os.path.abspath(output)


# пример использования:
if __name__ == "__main__":

    # print(yf.Ticker("MSFT").info)
    pprint.pprint(yf.Ticker("DE0006599905").info)
    domen = yf.Ticker("DE0006599905").info['website']
    print(norm_domain_from_website(domen))
    # norm_domen= norm_domain_from_website(domen)
    # path = fetch_clearbit_logo(norm_domen, size=256)
    # print("Логотип сохранён в:", path)



