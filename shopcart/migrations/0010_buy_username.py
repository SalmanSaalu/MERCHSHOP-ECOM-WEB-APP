# Generated by Django 3.2.7 on 2022-03-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0009_delete_ti'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='username',
            field=models.CharField(default='not given', max_length=100),
        ),
    ]
