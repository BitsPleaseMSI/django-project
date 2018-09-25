# Generated by Django 2.1.1 on 2018-09-10 15:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20180910_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this Particular book', primary_key=True, serialize=False, unique=True),
        ),
    ]