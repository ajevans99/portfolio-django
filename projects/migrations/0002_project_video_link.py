# Generated by Django 2.1.5 on 2019-03-23 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='video_link',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
