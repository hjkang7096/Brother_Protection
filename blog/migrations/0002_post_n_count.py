# Generated by Django 3.2.16 on 2023-01-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='n_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
