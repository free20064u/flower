# Generated by Django 3.2.1 on 2021-05-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_category_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='flower',
            name='tags',
            field=models.ManyToManyField(to='myapp.Tag'),
        ),
    ]
