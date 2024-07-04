import requests
import logging

logger = logging.getLogger(__name__)


def fetch_usd_to_rub_rate():
    """
        Функция для получения текущего курса доллара США к рублю из внешнего API.

        Возвращает:
            float: Текущий курс доллара США к рублю.
            None: Если произошла ошибка при запросе API.
        """
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        response.raise_for_status()
        data = response.json()
        return data['rates']['RUB']
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при получении курса валют: {e}")
        return None
