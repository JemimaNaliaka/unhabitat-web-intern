# Generated by Django 5.2.1 on 2025-05-14 21:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.TextField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
