# Generated by Django 4.2.1 on 2023-06-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('dpt_id', models.IntegerField()),
                ('c_name', models.CharField(max_length=100)),
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dpt',
            fields=[
                ('dpt_id', models.IntegerField(primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=100)),
            ],
        ),
    ]
