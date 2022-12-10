# Generated by Django 4.1.3 on 2022-12-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(blank=True, max_length=50, null=True)),
                ('telephone', models.CharField(max_length=50)),
                ('entreprise', models.BooleanField(default=False)),
            ],
        ),
    ]