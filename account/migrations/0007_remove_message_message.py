# Generated by Django 4.1.6 on 2023-02-17 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_message_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
    ]
