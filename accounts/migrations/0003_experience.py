# Generated by Django 4.2.5 on 2023-10-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_edjucation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('desc', models.TextField()),
            ],
        ),
    ]