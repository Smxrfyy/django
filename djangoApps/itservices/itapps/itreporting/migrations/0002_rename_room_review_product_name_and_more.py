# Generated by Django 4.2 on 2023-04-18 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itreporting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='room',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='type',
            new_name='product_review',
        ),
        migrations.RemoveField(
            model_name='review',
            name='details',
        ),
        migrations.AddField(
            model_name='review',
            name='product_rating',
            field=models.IntegerField(default=False, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(max_length=256),
        ),
    ]
