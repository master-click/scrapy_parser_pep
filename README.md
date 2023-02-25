# Асинхронный парсер документов PEP

## Технологии

1. Scrapy 2.5.1
2. Python 3.7.9


## Описание

Парсер собирает информацию обо всех PEP со страницы https://peps.python.org/.

Сохраняет данные в 2 csv файла.

В одном хранится список всех PEP: номер, название, статус.<br/>
Во втором содержится сводка по статусам PEP - количество PEP в каждом статусе и общее кол-во всех найденных документов.


## Запуск проекта

1. Клонируем проект

```
github clone git@github.com:master-click/scrapy_parser_pep.git
```

2. Создаем и активируем виртуальное окружение

```
python -m venv venv
source venv/Scripts/activate
```

3. Устанавливаем зависимости

```
pip install -r requirements.txt
```

4. Запуск парсера

```
scrapy crawl pep
```

5. Если все сделано правильно, в папке results должны появится 2 csv файла с данными.

## Разработчик
Студент Я.Практикума, Батова Ольга.