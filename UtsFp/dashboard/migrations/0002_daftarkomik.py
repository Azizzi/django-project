# Generated by Django 2.2.12 on 2022-11-25 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='daftarkomik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodekomik', models.CharField(max_length=8)),
                ('namakomik', models.CharField(max_length=120)),
                ('penerbit', models.CharField(max_length=50)),
            ],
        ),
    ]
