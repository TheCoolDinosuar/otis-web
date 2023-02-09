# Generated by Django 4.1.6 on 2023-02-09 22:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("arch", "0030_alter_vote_niceness"),
    ]

    operations = [
        migrations.AddField(
            model_name="vote",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="vote",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]