# Generated by Django 4.1.1 on 2022-12-14 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_date_alter_blog_description_alter_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
