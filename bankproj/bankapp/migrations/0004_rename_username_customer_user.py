# Generated by Django 4.2.5 on 2023-12-11 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0003_rename_user_customer_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='username',
            new_name='user',
        ),
    ]
