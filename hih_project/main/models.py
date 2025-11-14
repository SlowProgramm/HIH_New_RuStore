from django.db.models import CharField, TextField, Model

class Task(Model):
    title: CharField = CharField('Название', max_length=50)
    task: TextField = TextField('Описание')

    def __str__(self) -> str:
        return self.title
    