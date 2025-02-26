# Generated by Django 3.0.7 on 2020-07-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=33)),
                ('last_name', models.CharField(max_length=33)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=33)),
                ('email', models.CharField(max_length=33)),
                ('password', models.CharField(max_length=33)),
                ('phone', models.IntegerField()),
                ('qualification', models.CharField(max_length=40)),
            ],
        ),
    ]
