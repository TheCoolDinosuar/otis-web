# Generated by Django 4.0.7 on 2022-08-23 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0087_student_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='public',
        ),
    ]