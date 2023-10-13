# Generated by Django 4.2.5 on 2023-10-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_las_name_contact_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='contact',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
