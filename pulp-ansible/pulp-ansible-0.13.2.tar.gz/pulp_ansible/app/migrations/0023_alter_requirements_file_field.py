# Generated by Django 2.2.15 on 2020-09-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0022_URLField_to_CharField'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionremote',
            name='requirements_file',
            field=models.TextField(null=True),
        ),
    ]
