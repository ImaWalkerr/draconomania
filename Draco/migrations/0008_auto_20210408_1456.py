# Generated by Django 3.2 on 2021-04-08 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Draco', '0007_auto_20210408_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statslvl1translation',
            name='stats_lvl1',
        ),
        migrations.AddField(
            model_name='dragon',
            name='dmg',
            field=models.IntegerField(default=0, verbose_name='Урон'),
        ),
        migrations.AddField(
            model_name='dragon',
            name='exp',
            field=models.IntegerField(default=0, verbose_name='Опыт за получение'),
        ),
        migrations.AddField(
            model_name='dragon',
            name='gold',
            field=models.IntegerField(default=0, verbose_name='Золото/час'),
        ),
        migrations.AddField(
            model_name='dragon',
            name='hp',
            field=models.IntegerField(default=0, verbose_name='Здоровье'),
        ),
        migrations.AddField(
            model_name='dragon',
            name='points',
            field=models.IntegerField(default=0, verbose_name='Очки за сбор'),
        ),
        migrations.AddField(
            model_name='dragon',
            name='sale',
            field=models.IntegerField(default=0, verbose_name='Продажа'),
        ),
        migrations.AddField(
            model_name='dragontranslation',
            name='el1',
            field=models.TextField(default=1, max_length=20, verbose_name='Элемент 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dragontranslation',
            name='el2',
            field=models.TextField(default=1, max_length=20, verbose_name='Элемент 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dragontranslation',
            name='el3',
            field=models.TextField(default=1, max_length=20, verbose_name='Элемент 3'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='StatsLvl1',
        ),
        migrations.DeleteModel(
            name='StatsLvl1Translation',
        ),
    ]
