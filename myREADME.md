# Ссылки на репозитории для рецензента:
[Auth](https://github.com/NankuF/Auth_sprint_1)<br>
[Async_API_sprint_1](https://github.com/NankuF/Async_API_sprint_1)<br>

# Как запустить проект:

### 1. Скачать и запустить репозиторий [Auth](https://github.com/NankuF/Auth_sprint_1)<br>

Переименовать `.env.example` в `.env`

Развернуть сеть:
```bash
docker network create middle-practicum --subnet 172.18.0.0/24 --gateway 172.18.0.1 &&\
```
Pазвернуть volumes:

```bash
docker volume create postgresql-data &&\
docker volume create redis-auth
```
Запустить docker compose

### 2. Скачать и запустить репозиторий [ugc_sprint_1](https://github.com/NankuF/ugc_sprint_1)<br>

### 3. Скачать и запустить репозиторий [Async_API_sprint_1](https://github.com/NankuF/Async_API_sprint_1)<br>

Запуск проекта подробно описан в [README.md](https://github.com/NankuF/Async_API_sprint_1/blob/main/README.md) соответствующего проекта

### 4. В [Auth](https://github.com/NankuF/Auth_sprint_1) получить токен админа

Для этого:<br>
1) Перейти по ссылке http://127.0.0.1:82/api/openapi (или по http://127.0.0.1:82/api/openapi#/auth/login_api_v1_auth_login_post, тогда пропустить шаг 2))<br>
2) Отправить POST-запрос по ручке /api/v1/auth/login<br>
3) В теле запроса указать:<br>
```JSON
   {
    "username": "admin",
    "password": 123
   }
```
4) Ответ придет в форме:<br>
```JSON
{
    "access_token": "str",
    "refresh_token": "str",
    "token_type": "bearer"
}
```
### 5) Установить приложение [modheader](https://modheader.com/)<br><br>
### 6) Установить значения:<br><br>
   X-Request-Id: любая строка <br>
   User-Agent: Mozilla/5.0 (Android 10; Mobile; rv:125.0) Gecko/125.0 Firefox/125.0 <br>
   Authorization: bearer значение access_token, который скопировали в пункте 4
 ![alt text](<Screenshot from 2024-11-06 23-37-20.png>)

### 7) Перейти по ссылке http://127.0.0.1:81/api/openapi<br>
### 8) Отправлять запросы по ручкам в странице<br>
### 9) В [интерфейсе для управления Kafka](http://172.18.0.20:8080/ui/clusters/kraft/all-topics/messages/messages?keySerde=String&valueSerde=String&limit=100) проверить messages*<br>
 **не забывать обновлять страницу*


# Что поменялось в [Async_API_sprint_1](https://github.com/NankuF/Async_API_sprint_1)

1. Добавили KAFKA PRODUCER в middleware для отслеживания действий всех пользователей.
   + middleware отправляет сообщения в Kafka с информацией о каждом запросе, независимо от прав пользователя.
   + После формирования Kafka-сообщения middleware создает HTTP-запрос для отправки данных на сервис Kafka. Если статус ответа больше или равен 400, вызывается ошибка HTTPException.

2. Добавили KAFKA PRODUCER в check_permission, отслеживания действий и анализа поведения авторизованных пользователей.
   + Функция kafka_producer вызывается после получения ответа от запроса на проверку прав пользователя (response). Она передает в Kafka дополнительные данные о пользователе (user_id, полученный в resp).
