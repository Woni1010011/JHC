# Generated by Django 4.2.5 on 2023-09-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrot_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
