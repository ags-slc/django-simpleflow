# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 19:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected')], max_length=100)),
                ('approval_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('is_closed', models.BooleanField(default=False)),
                ('object_id', models.PositiveIntegerField()),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='auth.Group')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.AddField(
            model_name='approval',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='approval', to='simpleflow.Task'),
        ),
    ]