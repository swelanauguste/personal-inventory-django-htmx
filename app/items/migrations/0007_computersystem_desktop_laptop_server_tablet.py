# Generated by Django 5.0 on 2023-12-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_item_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('uid', models.CharField(blank=True, help_text='Unique ID', max_length=100, null=True, unique=True, verbose_name='UID')),
                ('manufacturer', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('memory', models.IntegerField(default=8, help_text='RAM in GB')),
                ('hdd', models.IntegerField(default=100, help_text='HDD in GB')),
                ('description', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tags', models.ManyToManyField(blank=True, to='items.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Desktop',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('items.computersystem',),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('items.computersystem',),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('items.computersystem',),
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('items.computersystem',),
        ),
    ]
