# Generated by Django 3.2.9 on 2022-01-25 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mv', '0002_alter_answer_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
    ]
