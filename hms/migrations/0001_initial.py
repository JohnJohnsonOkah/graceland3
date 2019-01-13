# Generated by Django 2.1.5 on 2019-01-12 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('guest', models.CharField(max_length=100)),
                ('room', models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('family', 'Family')], max_length=20)),
                ('price', models.IntegerField()),
                ('payment_status', models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending')], max_length=20)),
                ('remark', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-time',),
            },
        ),
    ]