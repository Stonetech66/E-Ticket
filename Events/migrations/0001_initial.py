# Generated by Django 4.1.1 on 2022-10-18 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyTicket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qty', models.PositiveIntegerField(default=1)),
                ('emails', models.CharField(blank=True, max_length=9000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=400)),
                ('tags', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField()),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('approved', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('category', models.ManyToManyField(related_name='event_categories', to='Events.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='TrendingEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events', models.ManyToManyField(related_name='events', to='Events.event')),
            ],
        ),
        migrations.CreateModel(
            name='TicketPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_fees', to='Events.event')),
            ],
        ),
        migrations.CreateModel(
            name='OrderTicket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('completed', 'completed'), ('not completed', 'not completed')], default='not completed', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_orders', to='Events.event')),
                ('tickets', models.ManyToManyField(to='Events.buyticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='buyticket',
            name='event_ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Events.ticketprice'),
        ),
        migrations.AddField(
            model_name='buyticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]
