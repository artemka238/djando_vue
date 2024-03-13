# Generated by Django 4.1.7 on 2024-01-24 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cats', '0007_aboutcats_user_delete_catsforpeople'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.aboutcats')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
