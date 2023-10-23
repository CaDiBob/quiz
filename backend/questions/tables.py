import datetime

from piccolo.table import Table
from piccolo.columns import Integer, Text, Timestamptz



class Question(Table):
    number: int = Integer(unique=True)
    text: str = Text()
    answer: str = Text()
    created_at: datetime.datetime = Timestamptz()
