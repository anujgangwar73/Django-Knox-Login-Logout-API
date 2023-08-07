# Generated by Django 4.2.3 on 2023-08-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapi', '0010_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'other')]),
        ),
    ]
