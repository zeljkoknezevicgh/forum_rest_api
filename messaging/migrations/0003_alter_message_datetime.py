# Generated by Django 4.1.3 on 2022-12-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_rename_sent_to_message_receiver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]