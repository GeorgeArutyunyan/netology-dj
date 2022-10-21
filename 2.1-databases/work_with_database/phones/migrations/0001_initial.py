# Generated by Django 4.1.2 on 2022-10-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=1, max_digits=10)),
                ('image', models.URLField(max_length=150)),
                ('release_date', models.DateField(verbose_name='release_date')),
                ('lte_exists', models.BooleanField(verbose_name='lte_exists')),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
    ]
