# Generated by Django 5.0.4 on 2024-04-27 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finaces', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id_cliente',
        ),
        migrations.AlterField(
            model_name='cliente_producto',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 9, 51, 2, 89481)),
        ),
        migrations.AlterField(
            model_name='cliente_producto',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 9, 51, 2, 89481)),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 9, 51, 2, 89481)),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 9, 51, 2, 89481)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 9, 51, 2, 89481)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 9, 51, 2, 89481)),
        ),
        migrations.AlterField(
            model_name='tipo_transancciones',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 9, 51, 2, 105072)),
        ),
        migrations.AlterField(
            model_name='tipo_transancciones',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 9, 51, 2, 105072)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 9, 51, 2, 105072)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 9, 51, 2, 105072)),
        ),
    ]
