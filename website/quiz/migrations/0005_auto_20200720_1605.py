# Generated by Django 3.0.7 on 2020-07-20 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20200719_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Java',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quiestion', models.CharField(max_length=4000, null=True)),
                ('incorrect_option1', models.CharField(max_length=100, null=True)),
                ('incorrect_option2', models.CharField(max_length=100, null=True)),
                ('incorrect_option3', models.CharField(max_length=100, null=True)),
                ('correct', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
