# Generated by Django 3.2.4 on 2021-09-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(max_length=200)),
                ('tf_amount', models.IntegerField(default=0)),
                ('idf_amount', models.IntegerField(default=0)),
            ],
        ),
    ]
