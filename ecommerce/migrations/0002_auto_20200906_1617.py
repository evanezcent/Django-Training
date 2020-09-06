# Generated by Django 3.1 on 2020-09-06 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.user'),
            preserve_default=False,
        ),
    ]