# Generated by Django 3.2.7 on 2021-09-13 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_auto_20210913_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Dept_stu',
            new_name='Dept_stud',
        ),
    ]
