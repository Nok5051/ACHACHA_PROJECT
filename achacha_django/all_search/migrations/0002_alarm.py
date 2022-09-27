# Generated by Django 3.2.15 on 2022-09-27 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('alarm_id', models.AutoField(primary_key=True, serialize=False)),
                ('users_id', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('category', models.CharField(blank=True, max_length=45, null=True)),
                ('src', models.CharField(blank=True, max_length=100, null=True)),
                ('turn', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'alarm',
                'managed': False,
            },
        ),
    ]
