# Generated by Django 4.0 on 2022-12-02 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_alter_run_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='project_id',
            field=models.PositiveIntegerField(default=0, verbose_name='analyst'),
        ),
    ]
