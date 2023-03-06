# Generated by Django 4.1.7 on 2023-03-06 14:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='../imresizer-1677838586928_dfojm5', upload_to='images/')),
                ('teacher', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('starts_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('ends_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
            options={
                'ordering': ['starts_at'],
            },
        ),
    ]
