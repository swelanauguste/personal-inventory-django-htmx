# Generated by Django 5.0 on 2023-12-28 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_alter_item_options_remove_item_serial_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(blank=True, to='items.tag'),
        ),
    ]
