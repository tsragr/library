# Generated by Django 3.2.8 on 2021-10-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.IntegerField(),
        ),
    ]