# Generated by Django 4.1.6 on 2023-02-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default='2023/02/18 01:32:15'),
        ),
    ]
