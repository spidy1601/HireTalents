# Generated by Django 4.1.7 on 2023-04-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire_talents', '0015_alter_developerimage_answer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetail',
            name='detail_id',
            field=models.IntegerField(unique=True),
        ),
    ]
