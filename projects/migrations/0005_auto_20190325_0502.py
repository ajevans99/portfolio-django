# Generated by Django 2.1.7 on 2019-03-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20190325_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='external_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='preview_image_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='projects.Tag', verbose_name='list of tags'),
        ),
        migrations.AlterField(
            model_name='project',
            name='video_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
