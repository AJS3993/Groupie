# Generated by Django 2.2.6 on 2020-01-02 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20200102_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Event')),
            ],
        ),
    ]
