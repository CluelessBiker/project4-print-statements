# Generated by Django 3.2.13 on 2022-07-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artprints', '0002_auto_20220707_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='artprint',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
