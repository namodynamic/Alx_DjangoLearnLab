# Generated by Django 5.1.6 on 2025-02-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Librarian', 'Librarians'), ('Member', 'Member')], default='Member', max_length=20),
        ),
    ]
