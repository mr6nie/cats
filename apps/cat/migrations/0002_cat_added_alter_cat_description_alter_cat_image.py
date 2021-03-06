# Generated by Django 4.0.4 on 2022-04-29 11:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cat',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Description *необязательное поле'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='image',
            field=models.ImageField(blank=True, default='default_cat.png', upload_to='cats_images', verbose_name='Image *необязательное поле'),
        ),
    ]
