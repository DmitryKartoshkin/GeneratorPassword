# Generated by Django 4.1.5 on 2023-01-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_alter_password_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='service',
            field=models.TextField(max_length=50, verbose_name='Ресурс'),
        ),
    ]
