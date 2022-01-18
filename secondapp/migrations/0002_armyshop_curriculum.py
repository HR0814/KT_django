# Generated by Django 2.2.5 on 2022-01-18 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArmyShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Army_Shop',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]