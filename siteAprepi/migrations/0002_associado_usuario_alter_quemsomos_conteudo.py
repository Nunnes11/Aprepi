# Generated by Django 5.0.6 on 2024-06-22 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteAprepi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Associado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=250)),
                ('matricula', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='quemsomos',
            name='conteudo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
