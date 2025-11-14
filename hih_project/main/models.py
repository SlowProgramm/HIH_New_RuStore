from django.db.models import CharField, TextField, Model, IntegerField, PositiveBigIntegerField, FloatField, ImageField, DateTimeField, ForeignKey, CASCADE, PROTECT
from django.contrib.auth.models import User

def icon_path(_, filename: str) -> str:
    return f'icons/{filename}'


def app_developer_path(instance: 'AppDeveloper', filename: str) -> str:
    return f'app_developer_id{instance.id}/{filename}'


def app_path(instance: 'App', filename: str) -> str:
    return f'app_id{instance.id}/{filename}'


def app_preview_image_path(instance: 'AppPreviewImage', filename: str) -> str:
    return app_path(instance.app, f'preview_images/{filename}')


class Task(Model):
    title: CharField = CharField('Название', max_length=50)
    task: TextField = TextField('Описание')

    def __str__(self) -> str:
        return self.title
    