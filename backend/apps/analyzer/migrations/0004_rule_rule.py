# Generated by Django 5.0.2 on 2024-04-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0003_rule_vulnerability'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='rule',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
