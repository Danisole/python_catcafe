# Generated by Django 4.1.7 on 2023-05-06 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0013_alter_menus_ingredientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]
