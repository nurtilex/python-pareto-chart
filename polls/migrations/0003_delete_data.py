# Generated by Django 4.1.7 on 2023-03-19 15:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0002_data_rename_diagrams_diagram_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Data",
        ),
    ]
