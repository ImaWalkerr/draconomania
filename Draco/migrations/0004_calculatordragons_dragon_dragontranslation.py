# Generated by Django 3.2 on 2021-04-08 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Draco', '0003_auto_20210408_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dragon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='web_media/dragons', verbose_name='Изображение яйцо')),
                ('image2', models.ImageField(upload_to='web_media/dragons', verbose_name='Изображение взрослый')),
                ('image3', models.ImageField(upload_to='web_media/dragons', verbose_name='Изображение детёныша')),
                ('usual_pic', models.ImageField(upload_to='web_media/info/', verbose_name='Обычный редкость')),
            ],
            options={
                'verbose_name': 'Дракон',
                'verbose_name_plural': 'Драконы',
            },
        ),
        migrations.CreateModel(
            name='DragonTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('rarity', models.CharField(max_length=20, verbose_name='Редкость')),
                ('description1', models.TextField(max_length=1000, verbose_name='Описание')),
                ('description2', models.TextField(max_length=1000, verbose_name='Получение')),
                ('description3', models.TextField(max_length=1000, verbose_name='Разведение')),
                ('language', models.CharField(max_length=2, verbose_name='Язык')),
                ('dragon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Draco.dragon')),
            ],
            options={
                'verbose_name': 'Дракон перевод',
                'verbose_name_plural': 'Драконы перевод',
            },
        ),
        migrations.CreateModel(
            name='CalculatorDragons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=2, verbose_name='Язык')),
                ('dragon1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dragon1', to='Draco.dragontranslation')),
                ('dragon2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dragon2', to='Draco.dragontranslation')),
                ('result', models.ManyToManyField(to='Draco.DragonTranslation')),
            ],
            options={
                'verbose_name': 'Дракон для калькулятора',
                'verbose_name_plural': 'Драконы для калькулятора',
            },
        ),
    ]