# Generated by Django 4.1.3 on 2022-12-01 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_rename_lista_lista_compras'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lista_compras',
            old_name='producto',
            new_name='product',
        ),
    ]