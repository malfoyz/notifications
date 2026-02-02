# Микросервис уведомлений

---

## Стек:
- Python 3.13
- FastAPI
- Tortoise ORM
- PostgreSQL 16

---

## Запуск с использованием Docker

1. Скачть / склонировать репозиторий
```bash
git clone <ссылка>
```


2. Скопировать файл `.env.example` и вставить в корень проекта с названием `.env` (вручную или через консоль - на примере bash):
```bash
cp .env.example .env
```

3. Cборка и запуск
```bash
docker compose up --build
```

4. Очистка
```bash
docker compose down -v
```

5. Запуск тестов
```json
docker compose run --rm app pytest -v
```

---

## API эндпоинты (на примерах)

### Проверка работоспособности

`GET /ping`

### Регистрация

`POST /auth/register`

Тело запроса:
```json
{
  "username": "john"
}
```

### Логин (вход)
`POST /auth/login`

Тело запроса:
```json
{
  "username": "john"
}
```

### Обновление `access` токена
`POST /auth/refresh`

Тело запроса:
```json
{
  "refresh_token": "<refresh>"
}
```

### Создание уведомления
`POST /notifications`

Заголовки:
```http
Authorization: Bearer <access>
```
Тело запроса:
```json
{
  "type": "comment",
  "text": "Комментарий 1"
}
```

### Список своих уведомлений

`GET /notifications`

Заголовки:
```http
Authorization: Bearer <access>`
```

### Удаление своего уведомления

`DELETE /notifications/{id}`

Заголовки:
```http
Authorization: Bearer <access>`
```

---

## Примечание

- Конфигурации проекта вынесены в `app/settings`
- Коментарии и документацию к коду не стал писать, так как это считается плохой практикой.
- Было бы чуть больше времени, можно было бы добавить линтеры, дописать больше сценариев в тестах, добавить кэш и навести больше красоты.
