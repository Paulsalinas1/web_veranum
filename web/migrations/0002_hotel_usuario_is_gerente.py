# Generated by Django 5.0.6 on 2024-07-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripción', models.CharField(max_length=150)),
                ('foto', models.ImageField(upload_to='hotel')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_gerente',
            field=models.BooleanField(default=False, verbose_name='gerente'),
        ),
    ]
