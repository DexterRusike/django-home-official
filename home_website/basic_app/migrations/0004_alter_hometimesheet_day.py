# Generated by Django 4.1 on 2024-04-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("basic_app", "0003_alter_hometimesheet_day"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hometimesheet",
            name="day",
            field=models.CharField(
                choices=[
                    ("Monday", "MONDAY"),
                    ("Tuesday", "TUESDAY"),
                    ("Wednesday", "WEDNESDAY"),
                    ("Thursday", "THURSDAY"),
                    ("Friday", "FRIDAY"),
                    ("Saturday", "SATURDAY"),
                    ("Sunday", "SUNDAY"),
                ],
                default="Monday",
                max_length=164,
            ),
        ),
    ]
