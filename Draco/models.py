from django.db import models
from django.contrib.auth.models import User


class MainPageTranslation(models.Model):
    """Главная страница"""
    description1 = models.TextField('Описание_1', max_length=5000)
    description2 = models.TextField('Описание_2', max_length=5000)
    description3 = models.TextField('Описание_3', max_length=5000)
    description4 = models.TextField('Описание_4', max_length=5000)
    description5 = models.TextField('Описание_5', max_length=5000)
    language = models.CharField('Язык', max_length=2)

    def __str__(self):
        return self.description1

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class Dragon(models.Model):
    """Драконы"""
    image1 = models.ImageField('Изображение яйцо', upload_to="web_media/dragons")
    image2 = models.ImageField('Изображение взрослый', upload_to="web_media/dragons")
    image3 = models.ImageField('Изображение детёныша', upload_to="web_media/dragons")
    element1 = models.ImageField('Стихия 1', upload_to="web_media/elements/")
    element2 = models.ImageField('Стихия 2', upload_to="web_media/elements/")
    element3 = models.ImageField('Стихия 3', upload_to="web_media/elements/")
    rating = models.FloatField('Рейтинг', default=0)
    dmg = models.IntegerField('Урон', default=0)
    hp = models.IntegerField('Здоровье', default=0)
    gold = models.IntegerField('Золото/час', default=0)
    exp = models.IntegerField('Опыт за получение', default=0)
    sale = models.IntegerField('Продажа', default=0)
    points = models.IntegerField('Очки за сбор', default=0)
    usual_pic = models.ImageField('Обычный редкость', upload_to="web_media/info/")

    class Meta:
        verbose_name = 'Дракон'
        verbose_name_plural = 'Драконы'


class DragonTranslation(models.Model):
    """Драконы перевод"""
    name = models.CharField('Имя', max_length=20)
    rarity = models.CharField('Редкость', max_length=20)
    description1 = models.TextField('Описание', max_length=1000)
    description2 = models.TextField('Получение', max_length=1000)
    description3 = models.TextField('Разведение', max_length=1000)
    el1 = models.TextField('Элемент 1', max_length=20)
    el2 = models.TextField('Элемент 2', max_length=20)
    el3 = models.TextField('Элемент 3', max_length=20)
    dragon = models.ForeignKey(Dragon, on_delete=models.CASCADE)
    language = models.CharField('Язык', max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дракон перевод'
        verbose_name_plural = 'Драконы перевод'


class PicturesStats(models.Model):
    """Картинки характеристики"""
    pictures = models.CharField('Название картинки', max_length=20)
    attack_pic = models.ImageField('Атака', upload_to="web_media/elements/")
    hp_pic = models.ImageField('Здоровье', upload_to="web_media/elements/")
    gold_pic = models.ImageField('Золото', upload_to="web_media/elements/")
    xp_pic = models.ImageField('Опыт', upload_to="web_media/elements/")
    sale_pic = models.ImageField('Продажа', upload_to="web_media/elements/")
    points_pic = models.ImageField('Очки за выведение', upload_to="web_media/elements/")

    def __str__(self):
        return self.pictures

    class Meta:
        verbose_name = 'Картинки характеристики'
        verbose_name_plural = 'Картинки характеристик'


class Elements(models.Model):
    """Свойства элементов"""
    element = models.ImageField('Элемент', upload_to="web_media/elements/")
    lvl_needed = models.IntegerField('Требуемый уровень', default=0)
    hp = models.IntegerField('Скейлы здоровья', default=0)
    dmg = models.IntegerField('Скейлы атаки', default=0)
    gold_per_hour = models.IntegerField('Бонус золото/час', default=0)

    def __int__(self):
        return self.lvl_needed

    class Meta:
        verbose_name = 'Свойство элементов'
        verbose_name_plural = 'Свойства элементов'


class ElementsTranslation(models.Model):
    """Свойства элементов перевод"""
    name_element = models.TextField('Название', max_length=20)
    elements = models.ForeignKey(Elements, on_delete=models.CASCADE)
    language = models.CharField('Язык', max_length=2)

    def __str__(self):
        return self.name_element

    class Meta:
        verbose_name = 'Свойство элементов перевод'
        verbose_name_plural = 'Свойства элементов перевод'


class PICweb(models.Model):
    """Технические изображения"""
    image = models.ImageField('Изображение', upload_to="web_media/other")
    text = models.TextField('Описание', max_length=100)

    class Meta:
        verbose_name = 'Техническое изображение'
        verbose_name_plural = 'Технические изображения'


class CalculatorDragons(models.Model):
    """Калькулятор выведения драконов"""
    dragon1 = models.ForeignKey(DragonTranslation, related_name='dragon1', on_delete=models.CASCADE)
    dragon2 = models.ForeignKey(DragonTranslation, related_name='dragon2', on_delete=models.CASCADE)
    result = models.ManyToManyField(DragonTranslation)
    language = models.CharField('Язык', max_length=2)

    class Meta:
        verbose_name = 'Дракон для калькулятора'
        verbose_name_plural = 'Драконы для калькулятора'


class TheStrengthWeakness(models.Model):
    """Сила и слабость элементов"""
    strong1 = models.ImageField('Силен против1', upload_to="web_media/elements/")
    strong2 = models.ImageField('Силен против2', upload_to="web_media/elements/")
    strong3 = models.ImageField('Силен против3', upload_to="web_media/elements/")
    weak1 = models.ImageField('Слаб против1', upload_to="web_media/elements/")
    weak2 = models.ImageField('Слаб против2', upload_to="web_media/elements/")
    weak3 = models.ImageField('Слаб против3', upload_to="web_media/elements/")
    steady1 = models.ImageField('Устойчив к1', upload_to="web_media/elements/")
    steady2 = models.ImageField('Устойчив к2', upload_to="web_media/elements/")
    steady3 = models.ImageField('Устойчив к3', upload_to="web_media/elements/")
    defenseless1 = models.ImageField('Уязвим к1', upload_to="web_media/elements/")
    defenseless2 = models.ImageField('Уязвим к2', upload_to="web_media/elements/")
    defenseless3 = models.ImageField('Уязвим к3', upload_to="web_media/elements/")
    elements_info = models.ForeignKey(Elements, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сила и слабость элементов'
        verbose_name_plural = 'Силы и слабости элементов'


class TheStrengthWeaknessTranslation(models.Model):
    """Сила и слабость элементов перевод"""
    element_about = models.CharField('Элемент', max_length=20)
    strength_weakness = models.ForeignKey(TheStrengthWeakness, on_delete=models.CASCADE)
    language = models.CharField('Язык', max_length=2)

    def __str__(self):
        return self.element_about

    class Meta:
        verbose_name = 'Сила и слабость элементов перевод'
        verbose_name_plural = 'Силы и слабости элементов перевод'


class TypeFood(models.Model):
    """Виды еды"""
    image_food = models.ImageField('Еда картинка', upload_to="web_media/food")
    image_type_food = models.ImageField('Еда тип картинка', upload_to="web_media/food")
    lvl_farm = models.IntegerField('Уровень ферм', default=0)
    time_grows = models.FloatField('Время производства часов', default=0)
    food = models.IntegerField('Кол-во еды', default=0)
    xp = models.IntegerField('Опыт', default=0)
    gold_coast = models.IntegerField('Цена', default=0)

    class Meta:
        verbose_name = 'Вид продукций еды'
        verbose_name_plural = 'Виды продукций еды'


class TypeFoodTranslation(models.Model):
    """Виды еды перевод"""
    type_food = models.CharField('Название', max_length=20)
    food = models.ForeignKey(TypeFood, on_delete=models.CASCADE)
    language = models.CharField('Язык', max_length=2)

    def __str__(self):
        return self.type_food

    class Meta:
        verbose_name = 'Вид продукций еды перевод'
        verbose_name_plural = 'Виды продукций еды перевод'


class AmountOfFood(models.Model):
    """Другие способы получения еды"""
    small = models.IntegerField('Максимальное кол-во', default=0)
    big = models.IntegerField('Минимальное кол-во', default=0)

    class Meta:
        verbose_name = 'Другой способ получения еды'
        verbose_name_plural = 'Другие способы получения еды'


class AmountOfFoodTranslation(models.Model):
    """Другие способы получения еды перевод"""
    methods = models.TextField('Методы получения', max_length=100)
    about = models.TextField('Примечания', max_length=2000)
    amount = models.ForeignKey(AmountOfFood, on_delete=models.CASCADE)
    language = models.CharField('Язык', max_length=2)

    def __str__(self):
        return self.methods

    class Meta:
        verbose_name = 'Другой способ получения еды перевод'
        verbose_name_plural = 'Другие способы получения еды перевод'


class InfoFoodTranslation(models.Model):
    """Информация еда перевод"""
    title_1 = models.TextField('Заголовок', max_length=100)
    title_2 = models.TextField('Инфа 1', max_length=1000)
    title_3 = models.TextField('Инфа 2', max_length=1000)
    language = models.CharField('Язык', max_length=2)

    def __str__(self):
        return self.title_1

    class Meta:
        verbose_name = 'Информация о ресурсе еда перевод'
        verbose_name_plural = 'Информация о ресурсе еда перевод'


class DopInfoElements(models.Model):
    """Описание элеменов"""
    image_info_el1 = models.ImageField('Картинка1', upload_to="web_media/info")
    image_info_el2 = models.ImageField('Картинка2', upload_to="web_media/info")
    image_info_el3 = models.ImageField('Картинка3', upload_to="web_media/info")

    class Meta:
        verbose_name = 'Дополнительная информация по элементу'
        verbose_name_plural = 'Дополнительная информация по элементам'


class DopInfoElementsTranslation(models.Model):
    """Описание элеменов перевод"""
    title_1 = models.TextField('Заголовок', max_length=100)
    title_2 = models.TextField('Инфа 1', max_length=10000)
    title_3 = models.TextField('Инфа 2', max_length=10000)
    title_4 = models.TextField('Инфа 3', max_length=10000)
    dop_info = models.ForeignKey(DopInfoElements, on_delete=models.CASCADE)
    language = models.CharField('Язык', max_length=2)

    def __str__(self):
        return self.title_1

    class Meta:
        verbose_name = 'Дополнительная информация по элементу перевод'
        verbose_name_plural = 'Дополнительная информация по элементам перевод'


class UsInfoTranslation(models.Model):
    """Дополнительная информация перевод"""
    title_1 = models.TextField('Заголовок', max_length=100)
    title_2 = models.TextField('Инфа 1', max_length=10000)
    title_3 = models.TextField('Инфа 2', max_length=10000)
    language = models.CharField('Язык', max_length=2)

    def __str__(self):
        return self.title_1

    class Meta:
        verbose_name = 'Дополнительная информация перевод'
        verbose_name_plural = 'Дополнительная информация перевод'


class SchoolsSymbolsTranslation(models.Model):
    """Информация о символах"""
    schools = models.TextField('Школы символов', max_length=100)
    info_school = models.TextField('Информация о школе', max_length=5000)
    symbol_1 = models.TextField('Тип символа', max_length=50)
    info_symbol_1 = models.TextField('Информация о символе', max_length=1000)
    symbol_2 = models.TextField('Тип символа', max_length=50)
    info_symbol_2 = models.TextField('Информация о символе', max_length=1000)
    symbol_3 = models.TextField('Тип символа', max_length=50)
    info_symbol_3 = models.TextField('Информация о символе', max_length=1000)
    symbol_4 = models.TextField('Тип символа', max_length=50)
    info_symbol_4 = models.TextField('Информация о символе', max_length=1000)
    symbol_5 = models.TextField('Тип символа', max_length=50)
    info_symbol_5 = models.TextField('Информация о символе', max_length=1000)
    language = models.CharField('Язык', max_length=2)

    def __str__(self):
        return self.schools

    class Meta:
        verbose_name = 'Информация о школе символе'
        verbose_name_plural = 'Информация о школах символов'


class Client(models.Model):
    """Расширение юзера"""
    address = models.CharField('Адрес', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Catalogs(models.Model):
    """Каталоги"""
    name_catalog = models.TextField('Тип каталога', max_length=200)

    def __str__(self):
        return self.name_catalog

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'


class Products(models.Model):
    """Товары"""
    image_product_main = models.ImageField('Изображение продукта основное', upload_to="web_media/info")
    image_product_1 = models.ImageField('Изображение продукта_1', upload_to="web_media/info")
    image_product_2 = models.ImageField('Изображение продукта_2', upload_to="web_media/info")
    catalogs = models.ForeignKey(Catalogs, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductsTranslation(models.Model):
    """Товары перевод"""
    name = models.CharField('Имя продукта', max_length=250)
    price = models.FloatField('Цена за продукт', default=0)
    old_price = models.FloatField('Старая цена за продукт', default=0)
    rating = models.FloatField('Рейтинг набора', default=0)
    value = models.IntegerField('Кол-во продукта', default=0)
    content = models.TextField('Контент', max_length=1000)
    products_info = models.ForeignKey(Products, on_delete=models.CASCADE)
    language = models.CharField('Язык', max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ перевод'
        verbose_name_plural = 'Заказы перевод'


class Orders(models.Model):
    """Заказы + данные пользовтеля"""
    username = models.TextField('Имя пользователя', max_length=20)
    phone = models.CharField('Номер телефона', max_length=20)
    email = models.CharField('email', max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Заказ + данные пользователя'
        verbose_name_plural = 'Заказы + данные пользователя'
