# Generated by Django 3.2.9 on 2022-10-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gr_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_mobile',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_roll',
            field=models.CharField(max_length=10),
        ),
    ]
