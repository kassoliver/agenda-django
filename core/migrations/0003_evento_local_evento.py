# Generated by Django 3.2.8 on 2021-11-02 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211024_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local_evento',
            field=models.TextField(blank=True, null=True),
        ),
    ]
