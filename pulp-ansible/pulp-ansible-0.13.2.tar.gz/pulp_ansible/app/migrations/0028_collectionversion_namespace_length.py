# Generated by Django 2.2.17 on 2021-01-25 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0027_tag_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionversion',
            name='namespace',
            field=models.CharField(editable=False, max_length=64),
        ),
    ]
