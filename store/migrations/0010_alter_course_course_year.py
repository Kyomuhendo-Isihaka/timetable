# Generated by Django 5.0 on 2024-06-17 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_course_course_lecturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_year',
            field=models.CharField(max_length=40),
        ),
    ]
