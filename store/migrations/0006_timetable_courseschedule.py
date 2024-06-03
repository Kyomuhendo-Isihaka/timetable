# Generated by Django 5.0 on 2024-06-02 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_student_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.program')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.course')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.room')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.staff')),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.timeslot')),
                ('timetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.timetable')),
            ],
        ),
    ]
