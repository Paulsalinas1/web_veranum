# Generated by Django 5.0.6 on 2024-07-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('correo', models.EmailField(max_length=150, primary_key=True, serialize=False, verbose_name='correo')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('is_staff', models.BooleanField(default=False, verbose_name='empleado')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser')),
                ('es_baneado', models.BooleanField(default=False, verbose_name='baneado')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]