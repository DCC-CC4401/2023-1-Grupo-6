# Generated by Django 4.2 on 2023-05-06 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_alter_user_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='contenido',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='nombre_producto',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='puntuacion',
            new_name='punctuation',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='cantidad_votantes',
            new_name='votes',
        ),
        migrations.RemoveField(
            model_name='review',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='review',
            name='nick_autor',
        ),
        migrations.AddField(
            model_name='review',
            name='creation_date',
            field=models.DateField(default='2023-05-06'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='fecha_creacion',
            field=models.DateField(default='2023-05-06'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
