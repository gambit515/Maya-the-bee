# Generated by Django 4.1.7 on 2023-04-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_anketa_status_remove_users_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фотография'),
        ),
    ]
