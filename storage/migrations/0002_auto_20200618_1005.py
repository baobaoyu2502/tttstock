# Generated by Django 3.0.3 on 2020-06-18 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stockOuthis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.CharField(default='tuotuo', max_length=20)),
                ('itemNo', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=20)),
                ('recordtime', models.CharField(default='tuotuo', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='stockinhis',
            name='recordtime',
            field=models.CharField(default='tuotuo', max_length=50),
        ),
    ]
