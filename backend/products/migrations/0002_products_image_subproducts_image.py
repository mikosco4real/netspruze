# Generated by Django 4.0.4 on 2022-08-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='subproducts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]