# Generated by Django 4.1.4 on 2023-02-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_canteen_c_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
