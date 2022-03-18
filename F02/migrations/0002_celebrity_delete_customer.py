# Generated by Django 4.0.3 on 2022-03-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('F02', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('worth', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
