# Generated by Django 2.1 on 2018-08-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.TextField(default='NULL'),
        ),
        migrations.AddField(
            model_name='book',
            name='publication',
            field=models.TextField(default='NULL'),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.TextField(default='NULL'),
        ),
    ]