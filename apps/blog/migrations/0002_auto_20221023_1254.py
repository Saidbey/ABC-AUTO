# Generated by Django 3.2.5 on 2022-10-23 12:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='company',
        ),
        migrations.RemoveField(
            model_name='news',
            name='company',
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
