# Generated by Django 5.0.3 on 2024-04-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_no', models.BigIntegerField()),
                ('message', models.TextField()),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
