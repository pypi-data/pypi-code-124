# Generated by Django 2.2.3 on 2019-08-26 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0010_ansible_related_names'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collectionimport',
            options={'ordering': ['task__created']},
        ),
        migrations.RemoveField(
            model_name='collectionimport',
            name='_created',
        ),
        migrations.RemoveField(
            model_name='collectionimport',
            name='_id',
        ),
        migrations.RemoveField(
            model_name='collectionimport',
            name='_last_updated',
        ),
        migrations.AlterField(
            model_name='collectionimport',
            name='task',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='+', serialize=False, to='core.Task'),
        ),
    ]
