# Generated by Django 3.0.8 on 2020-07-19 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maids', '0005_auto_20200718_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maid',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maid',
            name='certificate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maid',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maid',
            name='profile_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='maid',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
