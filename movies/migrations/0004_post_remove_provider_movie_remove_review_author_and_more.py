# Generated by Django 4.2.5 on 2024-10-31 00:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('poster_url', models.URLField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='provider',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Provider',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AlterField(
            model_name='list',
            name='movies',
            field=models.ManyToManyField(to='movies.post'),
        ),
    ]