# Generated by Django 5.1.1 on 2024-10-29 13:04

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0003_process_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='process',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='processes', to='Pages.service'),
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_image', models.ImageField(upload_to='image/')),
                ('timeframe', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('approach', models.TextField()),
                ('solution', models.TextField()),
                ('left_big_image', models.ImageField(upload_to='image/')),
                ('left_small_image1', models.ImageField(upload_to='image/')),
                ('left_small_image2', models.ImageField(upload_to='image/')),
                ('requirements', models.TextField()),
                ('challenge', models.TextField()),
                ('result', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='Pages.casecategory')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='Pages.client')),
            ],
        ),
    ]