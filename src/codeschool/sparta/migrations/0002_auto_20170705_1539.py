# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-05 15:39
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sparta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('user_evaluated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_evaluated', to=settings.AUTH_USER_MODEL)),
                ('user_evaluatee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_evaluatee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usergrade',
            name='post_grade',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='usergrade',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_grades', to='sparta.SpartaActivity'),
        ),
    ]