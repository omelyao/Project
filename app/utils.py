import csv
from typing import Any
import requests

from .types import Table, Item, Data


def get_table(path) -> tuple[list[Any], list[list[Any]]]:
    header = []
    body = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            if len(header) == 0:
                header += [*row]
                continue
            body.append([*row])

    return header, body


def get_context(items):
    data = []
    for item in items:
        table = Table(item.title, *get_table(item.csv_file.path))
        data.append(
            Item(
                table=table,
                img=item.image_file.url if item.image_file else ''
            )
        )
    return data


def parser(name):
    data = []
    r = requests.get(f'https://api.hh.ru/vacancies/?text={name}')

    result = r.json()
    vacancies = result.get('items', [])
    vacancies = vacancies if len(vacancies) < 10 else vacancies[:10]

    for vac in vacancies:
        try:
            r = requests.get(f'https://api.hh.ru/vacancies/{vac.get("id")}')
            result = dict(r.json())
        except Exception as e:
            continue
        try:
            data.append(
                Data(
                    name=result.get('name'),
                    description=result.get('description'),
                    key_skills=", ".join([i.get('name') for i in result.get('key_skills')]),
                    employer=result.get('employer', {}).get('name'),
                    salary=result['salary']['from'] if result.get('salary') else '',
                    area=result.get('area', {}).get('name'),
                    published_at=result.get('published_at').split('T')[0]
                )
            )
        except Exception as e:
            pass
    return data
