# Generated by Django 5.1.7 on 2025-03-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmertoken',
            name='farmer_key',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
