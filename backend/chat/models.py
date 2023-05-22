from django.db import models
from django.contrib.auth.models import User 


class Room(models.Model):
    creator = models.ForeignKey(User, verbose_name = "создатель", on_delete = models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name = "участники", related_name = 'invited_user')
    date = models.DateTimeField(verbose_name = "дата создания", auto_now_add = True)

    class Meta:
        verbose_name = "комната чата"
        verbose_name_plural = "комнаты чатов"

class Chat(models.Model):
    room = models.ForeignKey(Room, verbose_name = "чат", on_delete = models.CASCADE)
    user = models.ForeignKey(User, verbose_name = "автор сообщения", on_delete = models.CASCADE)
    text = models.TextField(verbose_name = "текст сообщения", max_length = 300)
    date = models.DateTimeField(verbose_name = "дата отправки", auto_now_add = True)

    class Meta:
        verbose_name = "сообщения чата"
        verbose_name_plural = "сообщения чатов"
