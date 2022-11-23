# Generated by Django 4.1 on 2022-11-22 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_profile_location_skill"),
        ("projects", "0004_project_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(name="project", options={"ordering": ["create"]},),
        migrations.AddField(
            model_name="review",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="review", unique_together={("owner", "project")},
        ),
    ]
