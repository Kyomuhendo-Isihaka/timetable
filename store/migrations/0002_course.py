# Generated by Django 5.0 on 2024-03-22 19:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('credits', models.PositiveIntegerField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.program')),
            ],
        ),
    ]
