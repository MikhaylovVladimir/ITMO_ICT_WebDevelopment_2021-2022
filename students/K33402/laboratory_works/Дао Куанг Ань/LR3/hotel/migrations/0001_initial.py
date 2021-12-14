# Generated by Django 3.2.9 on 2021-12-01 16:59

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_register', models.DateField(default=django.utils.timezone.now)),
                ('date_checkin', models.DateField(default=django.utils.timezone.now)),
                ('date_checkout', models.DateField(default=django.utils.timezone.now)),
                ('time_checkin', models.TimeField(default=django.utils.timezone.now)),
                ('time_checkout', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('birthdate', models.DateField(default=django.utils.timezone.now)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Other', 'Other')], default='M', max_length=10)),
                ('tel', models.CharField(default='', max_length=12)),
                ('city', models.CharField(default='', max_length=50)),
                ('passport', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('salary', models.IntegerField(default=30000)),
                ('passport', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default='0')),
                ('type', models.CharField(choices=[('1', 'Single'), ('2', 'Double'), ('3', 'Triple')], default='1', max_length=6)),
                ('price', models.IntegerField(default=1000)),
                ('state', models.CharField(choices=[('+', 'Available'), ('-', 'Occupied')], default='+', max_length=9)),
                ('floor', models.SmallIntegerField(default=1)),
                ('id_client', models.ManyToManyField(through='hotel.Bill', to='hotel.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.employee')),
                ('id_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='id_employee',
            field=models.ManyToManyField(through='hotel.Schedule', to='hotel.Employee'),
        ),
        migrations.AddField(
            model_name='bill',
            name='id_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.client'),
        ),
        migrations.AddField(
            model_name='bill',
            name='id_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tel', models.CharField(blank=True, max_length=15, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
