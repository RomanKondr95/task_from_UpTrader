# Generated by Django 4.2.6 on 2023-10-31 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menuitem_menu_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='name',
        ),
    ]
