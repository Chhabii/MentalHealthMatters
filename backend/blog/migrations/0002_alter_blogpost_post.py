# Generated by Django 4.1.4 on 2022-12-14 07:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost", name="post", field=ckeditor.fields.RichTextField(),
        ),
    ]