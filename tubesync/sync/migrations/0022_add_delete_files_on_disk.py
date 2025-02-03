# Generated by pac

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0021_source_copy_channel_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='delete_files_on_disk',
            field=models.BooleanField(default=False, help_text='Delete files on disk when they are removed from TubeSync', verbose_name='delete files on disk'),
        ),
    ]