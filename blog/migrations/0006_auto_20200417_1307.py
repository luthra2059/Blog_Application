# Generated by Django 3.0.5 on 2020-04-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200417_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(1, 'Publish'), (0, 'Draft')], default=0),
        ),
    ]
