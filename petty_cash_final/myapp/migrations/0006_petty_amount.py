# Generated by Django 4.1.6 on 2023-02-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_mobile_log_emp_code_remove_log_cname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='petty_amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_present', models.IntegerField()),
            ],
        ),
    ]
