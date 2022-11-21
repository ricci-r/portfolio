# Generated by Django 4.1.3 on 2022-11-21 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_remove_portfolio_category_portfolio_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="portfolio",
            name="category",
        ),
        migrations.AddField(
            model_name="portfolio",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="portfolio.category",
            ),
        ),
    ]