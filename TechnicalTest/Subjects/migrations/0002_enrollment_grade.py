# Generated by Django 5.0.7 on 2024-08-01 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='grade',
            field=models.FloatField(null=True),
        ),
    ]
