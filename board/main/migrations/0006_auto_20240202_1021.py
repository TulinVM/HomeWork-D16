# Generated by Django 3.2 on 2024-02-02 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_ad_rubric'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subrubric',
            options={'ordering': ('super_rubric__order', 'super_rubric__name', 'order', 'name'), 'verbose_name': 'Подкатегория', 'verbose_name_plural': 'Подкатегории'},
        ),
        migrations.AlterModelOptions(
            name='superrubric',
            options={'ordering': ('order', 'name'), 'verbose_name': 'Главная', 'verbose_name_plural': 'Главные'},
        ),
    ]
