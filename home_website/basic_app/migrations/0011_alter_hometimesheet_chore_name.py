# Generated by Django 4.1 on 2024-04-18 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("basic_app", "0010_alter_hometimesheet_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hometimesheet",
            name="chore_name",
            field=models.TextField(),
        ),
    ]