# Generated by Django 3.2.4 on 2022-09-13 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('deleted', 'Deleted')], db_index=True, default='draft', max_length=51, verbose_name='Status'),
        ),
    ]
