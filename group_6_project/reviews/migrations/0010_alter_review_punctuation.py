# Generated by Django 4.2 on 2023-05-06 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_rename_contenido_review_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='punctuation',
            field=models.IntegerField(help_text='Puntuación'),
        ),
    ]