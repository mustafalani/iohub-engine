# Generated by Django 3.1.4 on 2020-12-28 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=32, unique=True)),
                ('channel_id', models.CharField(blank=True, default='7588526197.abcdef0123456789', editable=False, max_length=10, unique=True)),
                ('channel_creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
