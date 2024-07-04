# Generated by Django 4.2.13 on 2024-06-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=15000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('is_primary', models.BooleanField(default=True)),
                ('prep_time_span', models.IntegerField(default=0)),
                ('prep_time_human', models.IntegerField(default=0)),
                ('cook_time_span', models.IntegerField(default=0)),
                ('cook_time_human', models.IntegerField(default=0)),
            ],
        ),
    ]