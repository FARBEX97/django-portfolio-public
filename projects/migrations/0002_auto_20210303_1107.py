# Generated by Django 3.1.7 on 2021-03-03 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeproject',
            name='demo_link',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='codeproject',
            name='repo_link',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
