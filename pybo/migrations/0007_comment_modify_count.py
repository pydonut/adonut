# Generated by Django 4.0.3 on 2023-06-04 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20200507_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modify_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
