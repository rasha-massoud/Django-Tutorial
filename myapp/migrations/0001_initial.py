# Generated by Django 4.2.7 on 2023-11-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
                ('svgPath', models.CharField(max_length=800)),
                ('iElementClass', models.CharField(max_length=100)),
                ('iconColor', models.CharField(max_length=100)),
            ],
        ),
    ]