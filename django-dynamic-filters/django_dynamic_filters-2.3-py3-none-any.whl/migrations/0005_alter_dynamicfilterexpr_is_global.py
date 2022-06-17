# Generated by Django 4.0.5 on 2022-06-17 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynfilters', '0004_alter_dynamicfilterexpr_is_global_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamicfilterexpr',
            name='is_global',
            field=models.BooleanField(db_index=True, default=False, help_text='Make filter accessible to all.'),
        ),
    ]
