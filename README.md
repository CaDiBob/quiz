# Simple quiz application


### Как использовать:

[Docker](https://docs.docker.com/get-docker/) и [docker-compose](https://docs.docker.com/compose/install/) должны быть установлены.
- ### Клонировать [репозитой](https://github.com/CaDiBob/quiz) с кодом
```bash
git clone https://github.com/CaDiBob/quiz.git
```
- ### Настроить переменные окружения
переименовать `example.env` в `.env`, при необходимости указать свои настройки.

`example.env:`

- `POSTGRES_USER=testuser`
- `POSTGRES_PASSWORD=pass`
- `POSTGRES_DB=quiz`
- `POSTGRES_HOST=db`
- `POSTGRES_PORT=5432`
- `API_URL=https://jservice.io/api/random`

- ### Собрать контейнер
```bash
docker-compose build
```
- ### Применить миграции
```bash
docker-compose run fastapi sh -c 'piccolo forward all'
```
- ### Запустить контейнер
```bash
docker-compose up
```

После запуска контейнера приложение будет доступно по адресу http://127.0.0.1:8000/docs/

Принимает только POST запросы на http://127.0.0.1:8000/questions/

Формат запроса:
```json
{
  "questions_num": 1
}
```
`questions_num` количество вопросов которое вы хотите получить в ответе.

Ответ на запрос выше будет выглядеть так:
```json
[
  {
    "number": 150601,
    "text": "This sorceress was introduced into Arthurian legend as Arthur's healer by Geoffrey of Monmouth around 1150",
    "answer": "Morgana le Fey (or Morgan le Fay) (Morgaine accepted)"
  }
]
```
Если в базе данных нет записей ответ будет пустой объект:
```json
[]
```


[Тестовое задание.](https://docs.google.com/document/d/1MPStlOFfvF9YWEx-0I1EwvWE9paKkhvFWyq7tRvcdc0/edit)
