# Generated by Django 5.0.6 on 2025-01-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
