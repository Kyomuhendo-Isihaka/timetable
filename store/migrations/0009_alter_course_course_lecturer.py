# Generated by Django 5.0 on 2024-06-17 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_course_course_lecturer_staff_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.staff'),
        ),
    ]
