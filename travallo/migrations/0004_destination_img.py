# Generated by Django 3.2.4 on 2021-06-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travallo', '0003_rename_nane_destination_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='img',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]