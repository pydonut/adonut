# Generated by Django 4.0.3 on 2023-06-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_comment_answer_comment_voter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='modify_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]