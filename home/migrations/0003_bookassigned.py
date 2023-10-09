# Generated by Django 4.2.5 on 2023-10-03 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookAssigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_days', models.IntegerField(default=1)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('fine', models.IntegerField(default=0)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
    ]