# Generated by Django 4.0.3 on 2022-03-29 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steg', '0004_alter_lsbdecode_inputimagepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='lsbdecode',
            name='message',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
