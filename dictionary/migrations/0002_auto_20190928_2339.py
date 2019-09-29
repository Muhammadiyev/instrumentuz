# Generated by Django 2.2.5 on 2019-09-28 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property_unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('rotation_frequency', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='property_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_of_property_unit', to='dictionary.Property_unit'),
        ),
    ]
