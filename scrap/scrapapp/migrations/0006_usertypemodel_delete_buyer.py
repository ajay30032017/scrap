# Generated by Django 4.1 on 2023-07-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scrapapp", "0005_remove_buyer_pincode_buyer_password"),
    ]

    operations = [
        migrations.CreateModel(
            name="userTypeModel",
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
                ("userType", models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name="buyer",
        ),
    ]
