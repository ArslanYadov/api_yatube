# API Yatube
### Запрос
```
curl -H 'Accept: application/json' http://localhost:8000/api/v1/posts/
```
### Ответ
``` json
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2021-10-14T20:41:29.648Z",
    "image": "string",
    "group": 0
}
```
### Описание
API для социальной сети Yatube.
### Возможности
* Создавать, редактировать и удалять свои посты.
* Оставлять комментарии к постам.
* Подписывайться на авторов.
### Примеры
Для доступа к API необходим JWT токен, который можно получить передав ```username``` и ```password``` по следующему эндпоинту:
```/api/v1/jwt/create/```

Получив JWT токен можно использовать эндпоинты:
1. Для всех постов:
```api/v1/posts/```
2. Для определенного поста:
```/api/v1/posts/{id}/```
3. Для всех комментариев определенного поста:
```/api/v1/posts/{post_id}/comments/```
4. Для определенного комментария:
```/api/v1/posts/{post_id}/comments/{id}/```
5. Для всех групп:
```api/v1/groups/```
6. Для определенной группы:
```api/v1/groups/{id}/```
7. Для подписок:
```api/v1/follow/```

### Технологии
* Python 3.7
* Django 2.2.16
* Django DRF 3.12.4
## Запуск проекта в dev-режиме
- В корневой директории проекта создать файл ```.env``` и установить свои значения для ```SECRET_KEY``` и ```DEBUG```
``` python
SECRET_KEY = 'Your_secret_key'
DEBUG = True # for dev-mode
```
- Установить и активировать виртуальное окружение
``` bash
$ python -m venv venv
```
``` bash
$ source venv/Scripts/activate
```
``` bash
$ python -m pip install --upgrade pip
``` 
- Установить зависимости из файла requirements.txt
``` bash
$ pip install -r requirements.txt
```
- В папке с файлом manage.py выполнить миграции:
``` bash
$ python manage.py migrate
```
- Запустить dev-сервер:
``` bash
$ python manage.py runserver
```
## Автор
Арслан Ядов

E-mail: [Arslan Yadov](mailto:arslanyadov@yandex.ru?subject=%20API%20Yatube)
