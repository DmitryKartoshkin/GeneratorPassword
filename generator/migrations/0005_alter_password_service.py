# Generated by Django 4.1.5 on 2023-01-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0004_alter_password_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='service',
            field=models.CharField(max_length=50, verbose_name='Ресурс'),
        ),
    ]
