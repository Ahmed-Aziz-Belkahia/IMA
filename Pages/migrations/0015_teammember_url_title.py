# Generated by Django 5.1.1 on 2024-10-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0014_case_small_overview'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='url_title',
            field=models.SlugField(blank=True),
        ),
    ]