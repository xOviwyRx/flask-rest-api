# Веб-сервис на Flask с использованием REST API

## Использование Docker

### Настройка проекта

Создайте `.env` файл в корне репозитория:

```bash
cp .env.dev .env
```

Внесите при необходимости корректировки в переменные окружения.


### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up
```

При первом запуске данный процесс может занять несколько минут.

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```

### Инициализация проекта

Команды выполняются внутри контейнера приложения:

```bash
docker-compose exec app bash
```

#### При первом запуске контейнеров необходимо применить миграции:

```bash
flask db upgrade
```


#### Пример запроса к POST API сервиса:
```bash
curl --header "Content-Type: application/json" --request POST --data '{"questions_num":3}'  http://localhost:5000
```
Примечание: число questions_num не должно превышать 100


### Подключение к СУБД:
```bash
docker-compose exec db psql flask_db -U myuser
```
(flask_db - название БД, myuser - имя пользователя СУБД)

#### Показать список всех записей таблицы question:
```bash
SELECT * FROM question;
```

#### Вывести количество всех записей в таблице question:
```bash
SELECT COUNT(*) FROM question;
```

