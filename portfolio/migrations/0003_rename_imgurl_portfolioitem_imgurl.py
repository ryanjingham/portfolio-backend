# Generated by Django 5.0.2 on 2024-02-10 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_portfolioitem_imgurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolioitem',
            old_name='imgurl',
            new_name='imgUrl',
        ),
    ]
