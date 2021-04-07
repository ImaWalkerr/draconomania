from django.db import models


class Dragon(models.Model):
    """Драконы"""
    image_1 = models.ImageField('Изображение яйцо', upload_to="web_media/dragons/")
    image_2 = models.ImageField('Изображение взрослый', upload_to="web_media/dragons/")
    image_3 = models.ImageField('Изображение детёныша', upload_to="web_media/dragons/")
    usual_pic = models.ImageField('Обычный редкость', upload_to="web_media/info/")

    class Meta:
        verbose_name = 'Дракон'
        verbose_name_plural = 'Драконы'


class PICweb(models.Model):
    """Технические изображения"""
    image = models.ImageField('Изображение', upload_to="web_media/other")
    text = models.TextField('Описание', max_length=100)

    class Meta:
        verbose_name = 'Техническое изображение'
        verbose_name_plural = 'Технические изображения'


class PIC(models.Model):
    image_1 = models.ImageField('Изображение яйцо', upload_to="web_media/info/")
    image_2 = models.ImageField('Изображение взрослый', upload_to="web_media/info/")

    class Meta:
        verbose_name = 'Дракон'
        verbose_name_plural = 'Драконы'
