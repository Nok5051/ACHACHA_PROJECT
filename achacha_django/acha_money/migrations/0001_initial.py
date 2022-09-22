# Generated by Django 3.2.15 on 2022-09-21 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LostItems',
            fields=[
                ('lost_items_id_pk', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('get_name', models.CharField(blank=True, max_length=150, null=True)),
                ('get_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('category', models.CharField(blank=True, max_length=45, null=True)),
                ('get_place', models.CharField(blank=True, max_length=45, null=True)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('find_place', models.CharField(blank=True, max_length=45, null=True)),
                ('pickup_check', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'lost_items',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('posts_id_pk', models.AutoField(primary_key=True, serialize=False)),
                ('users_id', models.CharField(blank=True, max_length=45, null=True)),
                ('title', models.CharField(blank=True, max_length=45, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('parcel', models.CharField(blank=True, max_length=45, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=45, null=True)),
                ('lost_items_id', models.CharField(blank=True, max_length=45, null=True)),
                ('img_src', models.ImageField(blank=True, null=True, upload_to='acha_money/')),
                ('get_place', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'posts',
                'managed': False,
            },
        ),
    ]
