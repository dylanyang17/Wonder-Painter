# Generated by Django 2.1 on 2019-10-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('nickname', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=256)),
                ('avatar', models.ImageField(default='static/images/default.jpg', upload_to='static/images/')),
            ],
        ),
    ]
