# Generated by Django 4.2.3 on 2023-08-01 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapi', '0006_alter_user_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]
