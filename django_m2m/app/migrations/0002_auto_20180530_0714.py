# Generated by Django 2.0.5 on 2018-05-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Shopping',
        ),
        migrations.AddField(
            model_name='customer',
            name='products',
            field=models.ManyToManyField(through='app.Shopping', to='app.Product'),
        ),
    ]
