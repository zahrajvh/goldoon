# Generated by Django 4.2.4 on 2023-08-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, verbose_name='توضیحات')),
                ('photo', models.ImageField(upload_to='flower/')),
            ],
        ),
    ]
