# Generated by Django 5.0.3 on 2024-04-10 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_name', models.CharField(max_length=70)),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'tech_table',
            },
        ),
        migrations.CreateModel(
            name='Subtechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtech_name', models.CharField(max_length=80)),
                ('date', models.DateField(auto_now=True)),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.technology')),
            ],
            options={
                'db_table': 'subtech_table',
            },
        ),
    ]