# Generated by Django 3.1 on 2020-09-06 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20200906_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('stock', models.IntegerField()),
                ('size', models.CharField(max_length=20, null=True)),
                ('color', models.CharField(max_length=30, null=True)),
                ('img_url', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateField()),
                ('deleted_at', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.user'),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product'),
        ),
    ]
