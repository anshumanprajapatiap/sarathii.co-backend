# Generated by Django 3.2.2 on 2021-06-03 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appsarathii', '0003_auto_20210603_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='Phone',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='Zipcode',
            field=models.TextField(null=True),
        ),
    ]
