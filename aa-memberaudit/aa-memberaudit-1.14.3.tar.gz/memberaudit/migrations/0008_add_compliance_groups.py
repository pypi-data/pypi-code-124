# Generated by Django 3.2.11 on 2022-02-17 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("memberaudit", "0007_add_exports_permission"),
    ]

    operations = [
        migrations.CreateModel(
            name="ComplianceGroupDesignation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="auth.group"
                    ),
                ),
            ],
        ),
    ]
