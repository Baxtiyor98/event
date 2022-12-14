# Generated by Django 4.1.1 on 2022-10-05 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_remove_order_snack"),
    ]

    operations = [
        migrations.CreateModel(
            name="Place",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name="quantity",
            options={
                "verbose_name": "Snack",
                "verbose_name_plural": "Number of Snacks",
            },
        ),
        migrations.AddField(
            model_name="order",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateField(default="2022-05-08"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="finish_time",
            field=models.TimeField(default="18:22"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="start_time",
            field=models.TimeField(default="18:22"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="place",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="orders.place"
            ),
        ),
    ]
