# Generated by Django 4.0.10 on 2023-12-12 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField()),
                ('content', models.TextField(max_length=200)),
            ],
        ),
    ]
