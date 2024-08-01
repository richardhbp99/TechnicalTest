# Generated by Django 5.0.7 on 2024-08-01 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Security', '0002_alter_person_email_alter_person_id_person_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudent',
            fields=[
                ('id_student', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Security.person')),
            ],
            options={
                'db_table': 'T101Estudent',
            },
        ),
    ]
