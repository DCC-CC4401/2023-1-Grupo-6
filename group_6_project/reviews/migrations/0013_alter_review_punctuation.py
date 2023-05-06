# Generated by Django 4.2 on 2023-05-06 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_alter_review_punctuation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='punctuation',
            field=models.IntegerField(choices=[(1, 'ONE_STAR'), (2, 'TWO_STARS'), (3, 'THREE_STARS'), (4, 'FOUR_STARS'), (5, 'FIVE_STARS')], default=3, help_text='Puntuación'),
        ),
    ]
