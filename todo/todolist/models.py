from django.db import models
from pygments.lexers import get_all_lexers


LEXERS = [item for item in get_all_lexers() if item[1]]


class Post(models.Model):
    title = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=100, blank=True, default='')
    created_at = models.DateTimeField(default=False)
    created_by = models.ForeignKey(default=False)


    class Meta:
        ordering = ['created']
