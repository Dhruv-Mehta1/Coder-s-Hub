# Generated by Django 5.0.3 on 2024-04-15 17:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
        ('user', '0006_answer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('abstract', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('database', models.CharField(max_length=50)),
                ('tool', models.CharField(max_length=100)),
                ('document', models.CharField(max_length=150)),
                ('sourcecode', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('subtech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.subtechnology')),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.technology')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project_upload',
            },
        ),
    ]
