# Generated by Django 4.0.4 on 2022-11-06 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0012_cashbook_like_count_alter_cashbook_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='name',
            new_name='hashtag_name',
        ),
    ]