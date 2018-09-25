# Generated by Django 2.1.1 on 2018-09-09 16:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20180909_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ea4de595-722e-4734-8d31-ba8ad2e1c62e'), help_text='Unique ID for this Particular book', primary_key=True, serialize=False),
        ),
    ]
