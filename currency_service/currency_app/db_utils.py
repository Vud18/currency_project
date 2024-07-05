from django.utils import timezone
from .models import CurrencyRateRequest


class CurrencyRateService:
    """
    Класс для взаимодействия с запросами курса валют в базе данных.
    """

    @staticmethod
    def save_currency_rate(rate):
        """
        Метод для сохранения курса валют в базе данных.

        Аргументы:
            rate (float): Курс доллара США к рублю.
        """
        new_request = CurrencyRateRequest(rate=rate)
        new_request.save()

    @staticmethod
    def get_last_10_requests():
        """
        Метод для получения последних 10 запросов курса валют из базы данных.
        """
        return CurrencyRateRequest.objects.order_by('-timestamp')[:10]

    @staticmethod
    def is_request_too_soon():
        """
        Метод для проверки, был ли последний запрос менее 10 секунд назад.

        Возвращает:
            bool: True, если последний запрос был менее 10 секунд назад, иначе False.
            float: Время, которое нужно подождать до следующего запроса.
        """
        last_request = CurrencyRateRequest.objects.order_by('-timestamp').first()
        if last_request:
            time_since_last_request = (timezone.now() - last_request.timestamp).total_seconds()
            if time_since_last_request < 10:
                return True, 10 - time_since_last_request
        return False, 0
