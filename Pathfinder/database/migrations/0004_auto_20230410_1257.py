# Generated by Django 3.2.18 on 2023-04-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20230406_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modulepathway',
            old_name='courseID',
            new_name='pathwayID',
        ),
        migrations.RemoveField(
            model_name='modulepathway',
            name='mpType',
        ),
        migrations.AddField(
            model_name='modulepathway',
            name='mpCore',
            field=models.BooleanField(default=True),
        ),
    ]
