from django.contrib import admin
from .models import *


@admin.register(MainPageTranslation)
class MainPageTranslationAdmin(admin.ModelAdmin):
    list_display = ("id", "description1", "description2", "description3", "description4", "description5", "language")
    list_display_links = ("id",)


@admin.register(Dragon)
class PICAdmin(admin.ModelAdmin):
    list_display = ("id", "image1", "image2", "image3", "element1", "element2", "element3", "dmg", "hp", "gold", "exp",
                    "sale", "points", "rating", "usual_pic", "background")
    list_display_links = ("id",)


@admin.register(DragonTranslation)
class DragonTranslationAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity", "description1", "description2", "description3", "el1", "el2", "el3", "dragon",
                    "language")
    list_display_links = ("name",)


@admin.register(TextStatsTranslation)
class TextStatsTranslationAdmin(admin.ModelAdmin):
    list_display = ("text", "language")
    list_display_links = ("text",)


@admin.register(PicturesStats)
class PicturesStatsAdmin(admin.ModelAdmin):
    list_display = ("pictures", "attack_pic", "hp_pic", "gold_pic", "xp_pic", "sale_pic", "points_pic")
    list_display_links = ("pictures",)


@admin.register(ElementsHomes)
class ElementsHomesAdmin(admin.ModelAdmin):
    list_display = ("id", "element_1", "element_2", "element_3", "element_4", "element_5", "element_6", "element_7",
                    "element_8", "element_9", "element_10", "element_11", "element_12", "element_13")
    list_display_links = ("id",)


@admin.register(Elements)
class ElementsAdmin(admin.ModelAdmin):
    list_display = ("element", "lvl_needed", "hp", "dmg", "gold_per_hour")
    list_display_links = ("element",)


@admin.register(ElementsTranslation)
class ElementsTranslationAdmin(admin.ModelAdmin):
    list_display = ("name_element", "elements", "language")
    list_display_links = ("name_element",)


@admin.register(PICweb)
class PICwebAdmin(admin.ModelAdmin):
    list_display = ("image", "text")
    list_display_links = ("image",)


@admin.register(CalculatorDragons)
class CalculatorDragonsAdmin(admin.ModelAdmin):
    list_display = ("id", "dragon1", "dragon2", "language")
    list_display_links = ("id",)


@admin.register(TheStrengthWeakness)
class TheStrengthWeaknessAdmin(admin.ModelAdmin):
    list_display = ("id", "strong1", "strong2", "strong3", "weak1", "weak2", "weak3", "steady1", "steady2",
                    "steady3", "defenseless1", "defenseless2", "defenseless3", "elements_info")
    list_display_links = ("id",)


@admin.register(TheStrengthWeaknessTranslation)
class TheStrengthWeaknessTranslationAdmin(admin.ModelAdmin):
    list_display = ("element_about", "strength_weakness", "language")
    list_display_links = ("element_about",)


@admin.register(TypeFood)
class TheStrengthWeaknessAdmin(admin.ModelAdmin):
    list_display = ("id", "image_food", "image_type_food", "lvl_farm", "time_grows", "food", "xp", "gold_coast")
    list_display_links = ("id",)


@admin.register(TypeFoodTranslation)
class TypeFoodTranslationAdmin(admin.ModelAdmin):
    list_display = ("type_food", "food", "language")
    list_display_links = ("type_food",)


@admin.register(AmountOfFood)
class AmountOfFoodAdmin(admin.ModelAdmin):
    list_display = ("id", "small", "big")
    list_display_links = ("id",)


@admin.register(AmountOfFoodTranslation)
class AmountOfFoodTranslationAdmin(admin.ModelAdmin):
    list_display = ("methods", "about", "amount", "language")
    list_display_links = ("methods",)


@admin.register(InfoFoodTranslation)
class InfoFoodTranslationAdmin(admin.ModelAdmin):
    list_display = ("title_1", "title_2", "title_3", "language")
    list_display_links = ("title_1",)


@admin.register(DopInfoElements)
class DopInfoElementsAdmin(admin.ModelAdmin):
    list_display = ("id", "image_info_el1", "image_info_el2", "image_info_el3")
    list_display_links = ("id",)


@admin.register(DopInfoElementsTranslation)
class DopInfoElementsAdmin(admin.ModelAdmin):
    list_display = ("title_1", "title_2", "title_3", "title_4", "dop_info", "language")
    list_display_links = ("title_1",)


@admin.register(UsInfoTranslation)
class UsInfoTranslationAdmin(admin.ModelAdmin):
    list_display = ("title_1", "title_2", "title_3", "language")
    list_display_links = ("title_1",)


@admin.register(SchoolsSymbolsTranslation)
class SchoolsSymbolsTranslationAdmin(admin.ModelAdmin):
    list_display = ("schools", "info_school", "symbol_1", "info_symbol_1", "symbol_2", "info_symbol_2", "symbol_3",
                    "info_symbol_3", "symbol_4", "info_symbol_4", "symbol_5", "info_symbol_5")
    list_display_links = ("schools",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "user")
    list_display_links = ("id",)


@admin.register(Catalogs)
class CatalogsAdmin(admin.ModelAdmin):
    list_display = ("id", "name_catalog")
    list_display_links = ("id",)


@admin.register(Products)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "image_product_main", "image_product_1", "image_product_2", "catalogs")
    list_display_links = ("id",)


@admin.register(ProductsTranslation)
class ClientTranslationAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "old_price", "rating", "value", "content", "products_info", "language")
    list_display_links = ("name",)


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "phone", "email")
    list_display_links = ("id",)
