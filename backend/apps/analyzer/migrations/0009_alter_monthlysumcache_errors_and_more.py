# Generated by Django 5.0.2 on 2024-05-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0008_alter_benchmark_options_alter_benchmark_branch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlysumcache',
            name='errors',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='monthlysumcache',
            name='usage',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
