# Generated by Django 4.1.7 on 2023-05-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoderSocial', '0003_alter_post_user_relationship_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatars/default.png', upload_to=''),
        ),
    ]
