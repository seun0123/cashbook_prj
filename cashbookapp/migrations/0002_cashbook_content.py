# Generated by Django 4.1.1 on 2022-09-29 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashbook',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
