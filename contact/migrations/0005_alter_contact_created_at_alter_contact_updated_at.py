# Generated by Django 4.1.3 on 2022-12-12 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0004_contact_created_at_contact_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="created_at",
            field=models.DateTimeField(auto_created=True, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]