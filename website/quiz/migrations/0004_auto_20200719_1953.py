# Generated by Django 3.0.7 on 2020-07-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20200719_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='password1',
            field=models.CharField(max_length=40000, null=True),
        ),
    ]
