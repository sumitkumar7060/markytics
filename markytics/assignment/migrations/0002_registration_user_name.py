# Generated by Django 4.1.3 on 2022-12-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assignment", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="user_name",
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
