# Generated by Django 5.0.3 on 2024-03-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_news_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]