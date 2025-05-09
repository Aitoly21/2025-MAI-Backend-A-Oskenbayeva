# Beauty Academy
Курсовой проект по дисциплине «Программная инженерия».
##  Описание проекта
Beauty Academy — это веб-платформа, разработанная на фреймворке Django и предназначенная для онлайн-обучения в сфере визажа. Система реализует регистрацию и хранение профилей пользователей, структуру курсов и категорий, расписание занятий, а также отображение этих данных через REST API.
## Технологии
- Python 3.12
- Django 5.2
- PostgreSQL
- Docker / Docker Compose
- Gunicorn + Nginx
- HTML, curl
## Структура проекта
```bash
beautyacademy/
├── core/                 # Основное Django-приложение
├── beautyacademy/       # Настройки проекта
├── manage.py
├── Dockerfile
├── docker-compose.yml
└── Makefile

Установка и запуск
git clone https://github.com/your-username/beautyacademy.git
cd beautyacademy
make build
make up
make migrate
make createsuperuser

Далее открой в браузере: http://localhost:8000/admin/

API (GET/POST)
/api/profile/ — данные профиля
/api/courses/ — курсы
/api/categories/ — категории

Контейнеры:
Проект разворачивается через Docker Compose и включает:
db — PostgreSQL
web — Django
nginx — статика + proxy
healthcheck для всех сервисов