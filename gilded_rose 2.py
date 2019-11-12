# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            checkType(item)

def checkType(item):
    
    if item.name == "Aged Brie":
        t = Cheese(item.name, item.sell_in, item.quality)
        t.updateOneItem(item)

    if item.name == "Backstage passes to a TAFKAL80ETC concert":
        t = BackstagePasses(item.name, item.sell_in, item.quality)
        t.updateOneItem(item)

    if item.name == "Sulfuras, Hand of Ragnaros":
        t = LegendaryItems(item.name, item.sell_in, item.quality)
        t.updateOneItem(item)

    if item.name == "Conjured Mana Cake":
        t = ConjuredItems(item.name, item.sell_in, item.quality)
        t.updateOneItem(item)

class Item:

    def __init__(self, name, sell_in, quality):

        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):

        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class TypeOfItem(Item):

    def incrementQuality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def decrementQuality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def updateExpired(self, item):
        self.decrementQuality(item)

    def updateSellIn(self, item):
        item.sell_in = item.sell_in - 1

    def updateQuality(self, item):
        self.decrementQuality(item)

    def updateOneItem(self, item):
        self.updateQuality(item)
        self.updateSellIn(item)
        if item.sell_in < 0:
            self.updateExpired(item)

class Cheese(TypeOfItem):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def updateExpired(self, item):
        super().incrementQuality(item)

    def updateQuality(self, item):
        super().incrementQuality(item)

class BackstagePasses(TypeOfItem):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def updateExpired(self, item):
        item.quality = 0

    def updateQuality(self, item):

        super().incrementQuality(item)
        if item.sell_in <= 10:
            super().incrementQuality(item)
        if item.sell_in <= 5:
            super().incrementQuality(item)

class LegendaryItems(TypeOfItem):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def updateExpired(self, item):
        return

    def updateSellIn(self, item):
        return

    def updateQuality(self, item):
        return

class ConjuredItems(TypeOfItem):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def updateExpired(self, item):
        super().decrementQuality(item)
        super().decrementQuality(item)

    def updateQuality(self, item):
        super().decrementQuality(item)
        super().decrementQuality(item)
