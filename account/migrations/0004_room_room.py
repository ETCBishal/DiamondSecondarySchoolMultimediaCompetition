# Generated by Django 4.1.6 on 2023-02-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_message_rename_chatroom_room_name_remove_room_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room',
            field=models.CharField(default=41, max_length=10000000),
            preserve_default=False,
        ),
    ]
