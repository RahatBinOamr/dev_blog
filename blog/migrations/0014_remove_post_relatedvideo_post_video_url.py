# Generated by Django 5.0 on 2024-04-30 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_bookmark_unique_together_post_relatedvideo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='relatedVideo',
        ),
        migrations.AddField(
            model_name='post',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
