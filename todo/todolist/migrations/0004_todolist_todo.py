# Generated by Django 3.1.4 on 2021-01-15 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_remove_todolist_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='todo',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]