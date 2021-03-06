# Generated by Django 3.2.3 on 2021-06-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a game genre (e.g. Strategy)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Enter a brief description of the game', max_length=1000)),
                ('price', models.TextField(max_length=5)),
                ('genre', models.ManyToManyField(help_text='Select a genre for this book', to='BoardGameLand.Genre')),
            ],
        ),
    ]
