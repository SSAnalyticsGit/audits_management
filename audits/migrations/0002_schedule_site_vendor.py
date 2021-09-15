# Generated by Django 3.1.4 on 2021-09-11 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('audits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('representative', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=26, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(max_length=200, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('region', models.CharField(max_length=4, null=True)),
                ('contact', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=26, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='audits.client')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('SfA', 'Scheduled for Audit'), ('SfDL', 'Scheduled for Data-logging'), ('SfA&DL', 'Scheduled for Audit & Data-logging'), ('PS', 'Pending Schedule'), ('A', 'Audited'), ('DL', 'Data-logged'), ('A&DL', 'Audited & Data-logged')], max_length=100, null=True)),
                ('report_received', models.BooleanField(default=False)),
                ('sites', models.ManyToManyField(to='audits.Site')),
                ('vendors', models.ManyToManyField(to='audits.Vendor')),
            ],
        ),
    ]
