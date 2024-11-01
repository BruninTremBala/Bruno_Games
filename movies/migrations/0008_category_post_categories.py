# Generated by Django 4.2.5 on 2024-11-01 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='posts', to='movies.category'),
        ),
    ]
