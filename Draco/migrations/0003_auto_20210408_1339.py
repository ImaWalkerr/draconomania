# Generated by Django 3.2 on 2021-04-08 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Draco', '0002_auto_20210408_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dragontranslation',
            name='dragon',
        ),
        migrations.DeleteModel(
            name='CalculatorDragons',
        ),
        migrations.DeleteModel(
            name='Dragon',
        ),
        migrations.DeleteModel(
            name='DragonTranslation',
        ),
    ]
