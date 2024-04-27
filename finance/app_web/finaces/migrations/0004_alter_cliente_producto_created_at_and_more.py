# Generated by Django 5.0.4 on 2024-04-27 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finaces', '0003_alter_cliente_producto_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_producto',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 10, 45, 248306)),
        ),
        migrations.AlterField(
            model_name='cliente_producto',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 10, 45, 248306)),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 10, 45, 248306)),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 10, 45, 248306)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 10, 45, 248306)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 10, 45, 248306)),
        ),
        migrations.AlterField(
            model_name='tipo_transancciones',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 10, 45, 248306)),
        ),
        migrations.AlterField(
            model_name='tipo_transancciones',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 10, 45, 248306)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 10, 45, 248306)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 10, 45, 248306)),
        ),
    ]
