# Generated by Django 3.2.7 on 2022-01-16 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchboxapp', '0007_auto_20220115_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchshop',
            old_name='shopimage',
            new_name='shopimage1',
        ),
        migrations.AddField(
            model_name='merchshop',
            name='shopimage2',
            field=models.ImageField(blank=True, upload_to='shop'),
        ),
        migrations.AddField(
            model_name='merchshop',
            name='shopimage3',
            field=models.ImageField(blank=True, upload_to='shop'),
        ),
        migrations.AddField(
            model_name='merchshop',
            name='shopimage4',
            field=models.ImageField(blank=True, upload_to='shop'),
        ),
    ]
