# Generated by Django 2.2.16 on 2021-03-12 21:12

from django.db import migrations, models


def add_wound_healing_constant(apps, schema_editor):
    IntegerGameConstant = apps.get_model("game_constants", "IntegerGameConstant")
    IntegerGameConstant.objects.create(id="Amount Needed To Heal Wounds", value=750)
    IntegerGameConstant.objects.create(id="Max Wound Healing Per Day", value=75)


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IntegerGameConstant",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("value", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RunPython(
            add_wound_healing_constant, migrations.RunPython.noop, elidable=False
        ),
    ]
