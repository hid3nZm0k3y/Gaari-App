# Generated by Django 4.2.3 on 2023-07-13 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaari', '0006_make_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='make',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]
