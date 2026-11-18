import requests

from third_project.gateway import config

API = 'https://api.telegram.org/bot{token}/sendMessage'


def send(text: str) -> None:
    url = API.format(token=config.TOKEN)
    resp = requests.post(url, json={'chat_id': config.CHAT_ID, 'text': text}, timeout=5)
    resp.raise_for_status()
