# Generated by Django 5.2 on 2025-04-23 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='url',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='tecnologias',
        ),
    ]
