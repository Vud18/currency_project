import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import fetch_usd_to_rub_rate
from .db_utils import CurrencyRateService


logger = logging.getLogger(__name__)


@csrf_exempt
def get_current_usd(request):
    """
    Представление для обработки запросов на получение текущего курса доллара США к рублю.

    Возвращает:
        JsonResponse: Текущий курс доллара США к рублю и последние 10 запросов.
        JsonResponse: Сообщение об ошибке, если запросы слишком часты или произошла ошибка при запросе API.
    """
    try:
        too_soon, wait_time = CurrencyRateService.is_request_too_soon()
        if too_soon:
            return JsonResponse(
                {"error": f"Подождите как минимум {wait_time:.2f} секунд между запросами."},
                status=429
            )

        usd_to_rub_rate = fetch_usd_to_rub_rate()

        if usd_to_rub_rate is None:
            return JsonResponse({"error": "Не удалось получить курс валют. Попробуйте позже."}, status=500)

        CurrencyRateService.save_currency_rate(usd_to_rub_rate)

        last_requests = CurrencyRateService.get_last_10_requests()

        return JsonResponse({
            "current_rate": usd_to_rub_rate,
            "last_10_requests": list(last_requests.values('timestamp', 'rate'))
        })
    except Exception as e:
        logger.error(f"Произошла непредвиденная ошибка: {e}")
        return JsonResponse({"error": "Произошла непредвиденная ошибка. Попробуйте позже."}, status=500)
