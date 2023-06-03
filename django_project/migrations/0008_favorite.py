# Generated by Django 3.2.13 on 2022-11-29 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_project', '0007_auto_20221027_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Favorites', to='django_project.pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]