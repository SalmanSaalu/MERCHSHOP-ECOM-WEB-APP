# Generated by Django 3.2.7 on 2022-03-12 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchboxapp', '0013_subcatelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcatelog',
            name='maincategoryname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchboxapp.catelog'),
        ),
    ]