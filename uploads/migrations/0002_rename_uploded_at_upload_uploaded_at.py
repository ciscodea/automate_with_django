# Generated by Django 5.0.6 on 2024-06-03 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("uploads", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="upload",
            old_name="uploded_at",
            new_name="uploaded_at",
        ),
    ]
