# Generated by Django 4.2.4 on 2023-09-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0002_flower_type_flower_alter_flower_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='EN_name',
            field=models.CharField(default='unknown', max_length=70),
        ),
    ]
