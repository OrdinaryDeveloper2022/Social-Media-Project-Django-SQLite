# Generated by Django 3.2.16 on 2023-02-19 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_followerscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followerscount',
            name='user_follower',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
