# Generated by Django 5.0.3 on 2024-04-10 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={},
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={},
        ),
        migrations.AlterModelOptions(
            name='phone',
            options={},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={},
        ),
        migrations.AlterModelOptions(
            name='rolepermission',
            options={},
        ),
        migrations.AlterModelOptions(
            name='userrole',
            options={},
        ),
        migrations.AlterModelTable(
            name='address',
            table='addresses',
        ),
        migrations.AlterModelTable(
            name='permission',
            table='permissions',
        ),
        migrations.AlterModelTable(
            name='personaddress',
            table='person_addresses',
        ),
        migrations.AlterModelTable(
            name='personphone',
            table='person_phones',
        ),
        migrations.AlterModelTable(
            name='phone',
            table='phones',
        ),
        migrations.AlterModelTable(
            name='role',
            table='roles',
        ),
        migrations.AlterModelTable(
            name='rolepermission',
            table='roles_permissions',
        ),
        migrations.AlterModelTable(
            name='userrole',
            table='users_roles',
        ),
    ]