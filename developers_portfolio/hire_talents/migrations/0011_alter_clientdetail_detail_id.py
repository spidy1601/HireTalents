# Generated by Django 4.1.7 on 2023-04-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire_talents', '0010_rename_detail_clientdetail_detail_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetail',
            name='detail_id',
            field=models.IntegerField(unique=True),
        ),
    ]