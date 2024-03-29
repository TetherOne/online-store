[![Python 3.6](https://img.shields.io/badge/python-3.11-green.svg)](https://www.python.org/downloads/release/python-360/)
![Django 3.0](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)
![SQLAlchemy 2.0](https://img.shields.io/badge/SQLAlchemy-2.0.25-green.svg)


# Описание проекта


    Написаны API-шки для онлайн магазина. Взаимодейсвие с товарами,
    профилями, пользователями, заказами. Реализована регистрация,
    аутентификация с использованием JWT, выход из системы.

![Image alt](https://github.com/TetherOne/online_store/raw/master/github-pages/img_2.png)


# Техническая информация

  - Фреймворк FastAPI
  - Валидация Pydantic
  - Кеширование Redis
  - Миграции Alembic
  - ORM SQLAlchemy
  - База данных PostgreSQL + asyncpg

# Запуск проекта

## 1. Клонируйте репозиторий:
```
git clone https://github.com/TetherOne/online-store
```
## 2. Соберите docker-compose:
```
docker compose build
```
## 3. Запустите docker-compose:
```
docker compose up
```
## 4. Перейдите в браузер по ссылке:
```
http://127.0.0.1:8000/docs
```
