from django.db import models
from pygments.lexers import get_all_lexers


LEXERS = [item for item in get_all_lexers() if item[1]]


class Todolist(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    todo = models.CharField(max_length=100, blank=True, default='')
    complete = models.BooleanField(default=False)


    class Meta:
        ordering = ['created']
