# Generated by Django 5.1.3 on 2024-12-07 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('can_deactivate_accounts', 'Can activate/deactivate accounts')]},
        ),
    ]