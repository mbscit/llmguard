# Generated by Django 5.0.1 on 2024-01-28 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeanalyzer', '0005_engine_public_insecurepattern'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insecurepattern',
            old_name='engine',
            new_name='analyzer',
        ),
    ]
