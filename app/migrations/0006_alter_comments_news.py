# Generated by Django 3.2.4 on 2021-06-13 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_comments_creation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="news",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="app.news",
            ),
        ),
    ]
