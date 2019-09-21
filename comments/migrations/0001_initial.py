# Generated by Django 2.2.5 on 2019-09-20 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instruments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('text', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('instruments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instruments', to='instruments.Instrument')),
            ],
            options={
                'verbose_name': 'Коментарии',
                'verbose_name_plural': 'Коментарии',
            },
        ),
    ]
