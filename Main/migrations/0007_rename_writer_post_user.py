# Generated by Django 4.2.1 on 2023-06-14 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0006_rename_user_id_post_writer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="writer",
            new_name="user",
        ),
    ]