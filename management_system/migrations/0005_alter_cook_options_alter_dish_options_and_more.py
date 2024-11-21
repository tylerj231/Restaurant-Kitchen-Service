# Generated by Django 5.1.3 on 2024-11-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management_system", "0004_alter_cook_options_alter_dish_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cook",
            options={"verbose_name_plural": "cooks"},
        ),
        migrations.AlterModelOptions(
            name="dish",
            options={"verbose_name_plural": "dishes"},
        ),
        migrations.AlterField(
            model_name="dishtype",
            name="name",
            field=models.CharField(max_length=55),
        ),
    ]
