# Generated by Django 4.2.3 on 2023-07-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
