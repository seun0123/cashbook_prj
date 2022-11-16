from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_user_like_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='account/static/images/'),
        ),
    ]
