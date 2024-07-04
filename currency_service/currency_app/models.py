from django.db import models


class CurrencyRateRequest(models.Model):
    """
    Модель для хранения запросов курса доллара США к рублю.

    Атрибуты:
        timestamp (DateTimeField): Время запроса курса.
        rate (FloatField): Курс доллара США к рублю на момент запроса.
    """
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время запроса")
    rate = models.FloatField(verbose_name="Курс доллара к рублю")

    def __str__(self):
        """
        Возвращает строковое представление объекта CurrencyRateRequest.
        """
        return f"{self.timestamp}: {self.rate}"

    class Meta:
        """
        Метаданные модели.
        """
        verbose_name = "Запрос курса валюты"
        verbose_name_plural = "Запросы курса валюты"
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['-timestamp']),
        ]
