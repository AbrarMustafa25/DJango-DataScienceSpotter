# Generated by Django 4.2.15 on 2024-08-12 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('published_date', models.DateField()),
                ('isbn', models.CharField(max_length=13)),
                ('page_count', models.IntegerField()),
                ('cover_url', models.URLField(blank=True, null=True)),
                ('language', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('summary', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='authors.author')),
            ],
        ),
    ]
