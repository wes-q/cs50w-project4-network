# Generated by Django 4.2.1 on 2023-05-10 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0005_remove_post_handle_user_handle"),
    ]

    operations = [
        migrations.AddField(
            model_name="follow",
            name="is_followed",
            field=models.BooleanField(default=True),
        ),
    ]
