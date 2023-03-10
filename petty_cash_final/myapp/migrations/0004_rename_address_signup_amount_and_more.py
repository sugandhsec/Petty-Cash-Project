# Generated by Django 4.1.1 on 2023-01-26 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_log_current_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='address',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='mobile',
            new_name='emp_code',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='cname',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='purpose',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='take_photo',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='todepartment',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='tosee',
        ),
        migrations.AddField(
            model_name='signup',
            name='reason',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
