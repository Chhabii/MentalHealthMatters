# Generated by Django 4.1.4 on 2023-01-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_alter_customuser_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to="profile_pic/"),
        ),
    ]
