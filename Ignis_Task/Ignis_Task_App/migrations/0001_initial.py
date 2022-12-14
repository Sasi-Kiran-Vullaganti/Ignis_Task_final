# Generated by Django 4.1.2 on 2022-10-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=300)),
                ('event_date', models.DateField(max_length=300)),
                ('event_time', models.TextField(max_length=300)),
                ('event_image', models.ImageField(blank=True, upload_to='images/')),
                ('like', models.BooleanField(default=False)),
            ],
        ),
    ]
