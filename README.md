## Создать Docker compose

начинается с 172.18.0.15

\- kafka

\- clickhouse (TODO)

\- api (FastAPI)

\- | etl | <-

## FastAPI 

- создать приложение с одним эндпоинтом, 
- через постман отправить на этот эндпоинт json
- эндпоинт должен принять json и записать в топик кафки

&nbsp;

### Создать приложение с одним эндпоинтом

POST 

content-type application/json

api/v1/kafka/event

### Через постман отправить на этот эндпоинт json
```json
{
	"timestamp": "DateTime[UTC]"
	"user_id": "login"
	"payload": {"key": "value"}
}

```

###  Эндпоинт должен принять json и записать в топик кафки

написать код для записи json  в kafka


# Результат

1. Docker-compose.yml с тремя сервисами (api(заглушка), etl(заглушка), kafka, clickhouse)
2.  Работающее API на FastAPI


# Шаг 2
модифицировать **middleware** в кинотеатре для перехвата всех http событий и отправки в /proxy-api