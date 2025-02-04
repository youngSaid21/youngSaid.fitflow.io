# Generated by Django 4.2.6 on 2024-05-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("SalleDeSport", "0005_alter_modepaiement_cvc_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Jour",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("jour_de_la_semaine", models.CharField(max_length=12)),
            ],
        ),
        migrations.RemoveField(
            model_name="seance",
            name="dateCours",
        ),
        migrations.AddField(
            model_name="seance",
            name="jours",
            field=models.ManyToManyField(to="SalleDeSport.jour"),
        ),
    ]
