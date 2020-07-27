# x-one_test
Тестовое задание для вакансии от X-ONE

- Python 3.8
- Django 3

- Vue 2
- Vuetify

Локальный запуск:

Бэк:

1. (если не установлен poetry) `pip install poetry`
2. `poetry shell`
3. `poetry install --no-root`
4. копируем `.env.template` в `.env` (если не планируется использовать стороннюю БД, иначе изменяем данные)
5. `python manage.py migrate`
6. `python manage.py createsuperuser`

Фронт:

1. `yarn install` (из папки frontend)

Запуск:

1. `docker-compose -f docker-compose.dep.yml up` (поднимается БД)
2. `yarn serve` (из папки frontend)
3. `python manage.py runserver` (из виртуального окружения `poetry shell`)

Продакшен:

1. `docker-compose up`

Линтеры:

- `flake8 --config=setup.cfg`
- `black .`
- `isort .`
- `cd frontend && yarn lint`