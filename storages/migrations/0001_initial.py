# Generated by Django 4.0.6 on 2022-07-16 19:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the company.', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the storage.', max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storages.company')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the product.', max_length=70)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='Price of the product.')),
                ('description', models.TextField(blank=True, null=True)),
                ('upc', models.CharField(help_text='Universal product code of this product.', max_length=12)),
                ('quantity', models.IntegerField(default=0, verbose_name='The available quantity of the product.')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storages.storage')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
