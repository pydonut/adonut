# Generated by Django 4.0.3 on 2023-06-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0010_question_modify_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
