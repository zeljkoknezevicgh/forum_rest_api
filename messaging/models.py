from django.conf import settings
from django.db import models


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="asd2")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="asd")
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.receiver} {self.text} {self.sender} {self.datetime}"
