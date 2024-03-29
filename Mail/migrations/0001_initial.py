# Generated by Django 2.2.3 on 2019-07-16 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmailDate', models.DateField()),
                ('FromEmailId', models.CharField(max_length=50)),
                ('ToEmailId', models.CharField(max_length=50)),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('EmailId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=50)),
                ('Username', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
            ],
        ),
    ]
