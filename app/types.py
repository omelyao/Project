from typing import NamedTuple, List


class Table(NamedTuple):
    name: str
    header: List[str]
    body: List[str]


class Item(NamedTuple):
    table: Table
    img: str


class Data(NamedTuple):
    name: str
    description: str
    key_skills: str
    employer: str
    salary: str
    area: str
    published_at: str
