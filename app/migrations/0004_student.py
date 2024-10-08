# Generated by Django 5.1.1 on 2024-09-14 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('dpi', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('telefhone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('password_check', models.CharField(max_length=50)),
                ('username', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]
