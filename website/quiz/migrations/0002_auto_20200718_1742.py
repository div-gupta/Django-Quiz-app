# Generated by Django 3.0.7 on 2020-07-18 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=33, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='first_name',
            field=models.CharField(max_length=33, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='last_name',
            field=models.CharField(max_length=33, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=33, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='qualification',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=33, null=True),
        ),
    ]
