# Generated by Django 5.0 on 2024-02-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
