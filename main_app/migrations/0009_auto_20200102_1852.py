# Generated by Django 2.2.6 on 2020-01-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20200102_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.URLField(max_length=100),
        ),
    ]
