# Generated by Django 4.1.1 on 2022-11-30 15:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('mobile', models.PositiveIntegerField()),
                ('cname', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('tosee', models.CharField(max_length=100)),
                ('todepartment', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
