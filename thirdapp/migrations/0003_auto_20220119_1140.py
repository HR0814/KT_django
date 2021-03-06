# Generated by Django 2.2.5 on 2022-01-19 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0002_auto_20220119_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.AutoField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=14, null=True)),
                ('loc', models.CharField(max_length=13, null=True)),
            ],
            options={
                'db_table': 'dept',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=10, null=True)),
                ('job', models.CharField(max_length=9, null=True)),
                ('mgr', models.IntegerField(null=True)),
                ('hiredate', models.DateTimeField(null=True)),
                ('sal', models.IntegerField(null=True)),
                ('comm', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'emp',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='shop',
            table='shop',
        ),
    ]
