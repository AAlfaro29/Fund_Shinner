# Generated by Django 3.2.5 on 2021-09-22 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210914_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.JSONField(default=list),
        ),
    ]