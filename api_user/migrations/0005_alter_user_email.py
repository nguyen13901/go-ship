# Generated by Django 4.1.2 on 2022-10-30 19:03
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_user", "0004_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=255, verbose_name="Email"),
        ),
    ]
