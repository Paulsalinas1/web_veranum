# Generated by Django 5.0.6 on 2024-07-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_habitacion_precio_habitacion_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='foto',
            field=models.ImageField(default='null', null=True, upload_to='foto_h'),
        ),
    ]