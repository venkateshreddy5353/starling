# Generated by Django 3.2.4 on 2021-06-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=10, unique=True, verbose_name='user name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('phonenumber', models.CharField(max_length=10, verbose_name='phone number')),
                ('birthdate', models.DateField(verbose_name='birth date')),
                ('nickname', models.CharField(max_length=6, verbose_name='nick name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
