# Generated by Django 5.1.1 on 2024-10-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0011_client_bussiness_name_client_bussiness_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='image/')),
                ('role', models.CharField(max_length=50)),
                ('twitter', models.URLField(blank=True)),
                ('linked_in', models.URLField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
            ],
        ),
    ]
