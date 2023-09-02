# Generated by Django 4.2.4 on 2023-09-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SongsWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=150)),
                ('type_word', models.CharField(choices=[('G', 'Grave'), ('A', 'Aguda')], max_length=1)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('txt', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=150)),
                ('type_word', models.CharField(choices=[('G', 'Grave'), ('A', 'Aguda')], max_length=1)),
            ],
        ),
    ]
