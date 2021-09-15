# Generated by Django 3.2.5 on 2021-09-15 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(blank=True, max_length=255, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('identifier', models.CharField(max_length=55)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.division')),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=120)),
                ('name', models.CharField(max_length=120, unique=True)),
                ('cpu', models.CharField(max_length=120)),
                ('ram', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pole', models.CharField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software', models.CharField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('editor', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Os',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os', models.CharField(blank=True, max_length=120, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('type', models.CharField(max_length=120)),
            ],
            options={
                'unique_together': {('name', 'type')},
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine', models.CharField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('serial_number', models.CharField(max_length=255)),
                ('reference', models.CharField(max_length=255)),
                ('storage', models.IntegerField()),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.employee')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.model')),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.os')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.function'),
        ),
        migrations.AddField(
            model_name='employee',
            name='pole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.pole'),
        ),
        migrations.AddField(
            model_name='employee',
            name='software',
            field=models.ManyToManyField(blank=True, to='inventory.Software'),
        ),
    ]
