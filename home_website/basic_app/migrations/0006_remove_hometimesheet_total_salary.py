# Generated by Django 4.1 on 2024-04-14 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("basic_app", "0005_hometimesheet_total_salary"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hometimesheet",
            name="total_salary",
        ),
    ]
