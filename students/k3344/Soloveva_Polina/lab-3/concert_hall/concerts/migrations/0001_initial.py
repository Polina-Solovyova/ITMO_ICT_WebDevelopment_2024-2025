# Generated by Django 5.1.4 on 2025-01-14 16:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('manager', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='concerts.jpg', upload_to='concerts')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('age_limit', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('held', 'Проведен'), ('cancelled', 'Отменен'), ('pending', 'В ожидании'), ('in_progress', 'В работе')], max_length=11)),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concerts', to='concerts.performer')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_quantity', models.PositiveIntegerField()),
                ('sold_quantity', models.PositiveIntegerField(default=0)),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_categories', to='concerts.concert')),
            ],
            options={
                'unique_together': {('concert', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('confirmed', 'Подтверждено'), ('pending', 'В ожидании'), ('returned', 'Возврат')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='concerts.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='ConcertEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to='concerts.concert')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concerts', to='concerts.equipment')),
            ],
            options={
                'unique_together': {('concert', 'equipment')},
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizers', to='concerts.concert')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organized_concerts', to='concerts.employee')),
            ],
            options={
                'unique_together': {('employee', 'concert')},
            },
        ),
    ]
