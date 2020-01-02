# Generated by Django 2.2.6 on 2019-12-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_artist_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='bio',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='venue',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='event',
            name='sale',
        ),
        migrations.AddField(
            model_name='event',
            name='event_url',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='tickets',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
