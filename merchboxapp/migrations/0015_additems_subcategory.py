# Generated by Django 3.2.7 on 2022-03-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchboxapp', '0014_alter_subcatelog_maincategoryname'),
    ]

    operations = [
        migrations.AddField(
            model_name='additems',
            name='subcategory',
            field=models.CharField(default='null', max_length=100),
        ),
    ]