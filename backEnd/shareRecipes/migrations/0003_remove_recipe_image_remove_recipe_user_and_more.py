# Generated by Django 5.0.3 on 2024-04-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareRecipes', '0002_recipe_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='user',
        ),
        migrations.AddField(
            model_name='recipe',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]