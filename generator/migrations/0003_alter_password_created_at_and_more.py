# Generated by Django 4.1.5 on 2023-01-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_alter_password_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='password_for_the_service',
            field=models.CharField(max_length=20, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='password',
            name='service',
            field=models.TextField(max_length=100, verbose_name='Ресурс'),
        ),
        migrations.AlterField(
            model_name='password',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
