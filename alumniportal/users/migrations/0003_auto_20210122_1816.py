# Generated by Django 3.1.5 on 2021-01-22 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210112_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_active',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]