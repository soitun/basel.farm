# Generated by Django 2.0.2 on 2018-02-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0008_auto_20180217_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionGroupCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.PositiveIntegerField()),
            ],
        ),
    ]
