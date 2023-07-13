# Generated by Django 4.2.3 on 2023-07-11 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaari', '0003_alter_autos_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('content', models.TextField(max_length=100)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaari.autos')),
            ],
        ),
    ]
