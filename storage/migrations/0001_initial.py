# Generated by Django 3.0.3 on 2020-06-18 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.CharField(default='tuotuo', max_length=20)),
                ('itemNo', models.CharField(max_length=20)),
                ('type', models.CharField(default='m ', max_length=300)),
                ('partNo', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=20)),
                ('Vendor', models.CharField(max_length=20)),
                ('period', models.CharField(max_length=20)),
                ('cost', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='orderAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.CharField(default='tuotuo', max_length=20)),
                ('itemNo', models.CharField(max_length=20)),
                ('type', models.CharField(default='m ', max_length=300)),
                ('partNo', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='projectAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.CharField(default='tuotuo', max_length=20)),
                ('itemNo', models.CharField(max_length=20)),
                ('type', models.CharField(default='m ', max_length=300)),
                ('partNo', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='stockinhis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.CharField(default='tuotuo', max_length=20)),
                ('itemNo', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='stockRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.CharField(max_length=20)),
                ('itemNo', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=300)),
                ('partNo', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=20)),
                ('Vendor', models.CharField(max_length=20)),
                ('period', models.CharField(max_length=20)),
                ('cost', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=20)),
            ],
        ),
    ]
