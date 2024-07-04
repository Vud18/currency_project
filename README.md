# Currency Rate Service

Этот проект представляет собой веб-приложение на Django для получения текущего курса доллара США к рублю с использованием внешнего API. Приложение также сохраняет последние 10 запросов курса и обеспечивает минимальный интервал в 10 секунд между запросами.

## Установка

### 1. Клонируйте репозиторий

git clone https://github.com/Vud18/currency_project.git

Перейти в рабочий каталог
"cd currency-rate-service"

### 2. Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate # Для Windows: venv\Scripts\activate

pip install -r requirements.txt

### 3. Примените миграции
python manage.py migrate

### 4. Запустите сервер разработки
python manage.py runserver

Использование:
Перейдите по адресу http://127.0.0.1:8000/get-current-usd/ чтобы получить текущий курс доллара к рублю и последние 10 запросов.
