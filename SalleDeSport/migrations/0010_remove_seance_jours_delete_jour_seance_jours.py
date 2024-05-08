# Generated by Django 4.2.6 on 2024-05-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("SalleDeSport", "0009_alter_cours_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="seance",
            name="jours",
        ),
        migrations.DeleteModel(
            name="Jour",
        ),
        migrations.AddField(
            model_name="seance",
            name="jours",
            field=models.CharField(default="", max_length=12),
            preserve_default=False,
        ),
    ]
