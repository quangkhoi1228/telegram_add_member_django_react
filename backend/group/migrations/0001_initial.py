# Generated by Django 3.2.9 on 2021-11-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=100)),
                ('group_id', models.CharField(max_length=100)),
            ],
        ),
    ]
