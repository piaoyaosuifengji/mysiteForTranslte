# Generated by Django 2.0.4 on 2018-05-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='translte_str',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_text', models.CharField(max_length=3500)),
                ('tranlate_text', models.CharField(max_length=3500)),
            ],
        ),
    ]
