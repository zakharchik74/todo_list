# Generated by Django 4.0.5 on 2022-07-26 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_todo_process_user_delete_todo_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
