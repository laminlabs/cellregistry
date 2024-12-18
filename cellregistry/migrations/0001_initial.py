# Generated by Django 5.1.1 on 2024-10-18 23:48

import django.db.models.deletion
import lnschema_core.ids
import lnschema_core.models
import lnschema_core.users
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("lnschema_core", "0068_alter_artifactulabel_unique_together_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cell",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=lnschema_core.ids.base62_20, max_length=20, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, default=None, max_length=255, unique=True
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        db_index=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "_previous_runs",
                    models.ManyToManyField(related_name="+", to="lnschema_core.run"),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.run",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(lnschema_core.models.CanCurate, models.Model),
        ),
        migrations.CreateModel(
            name="ArtifactCell",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "artifact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links_cell",
                        to="lnschema_core.artifact",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.run",
                    ),
                ),
                (
                    "cell",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links_artifact",
                        to="cellregistry.cell",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(lnschema_core.models.LinkORM, models.Model),
        ),
    ]
