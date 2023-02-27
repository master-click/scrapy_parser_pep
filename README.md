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

5. Если все сделано правильно, в папке results должны появиться 2 csv файла с данными.

## Примеры работы парсера

1. Файл **results/pep_2023-02-25T11-31-34.csv**

```
number,name,status
213,Attribute Access Handlers,Deferred
1,PEP Purpose and Guidelines,Active
219,Stackless Python,Deferred
220,"Coroutines, Generators, Continuations",Rejected
212,Loop Counter Iteration,Rejected
216,Docstring Format,Rejected
...
...
...
```

2. Файл **results/status_summary_2023-02-25_14-31-49.csv**

```
Статус,Количество
Deferred,36
Active,31
Rejected,120
Final,269
Superseded,20
Withdrawn,55
Accepted,44
Draft,29
April Fool!,1
Total,605
```

## Разработчик
Студент Я.Практикума, Батова Ольга.
