# Generated by Django 3.1.7 on 2021-03-02 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pical_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
