class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        #At the end of each day our system lowers both values for every item
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
                #“Conjured” items degrade in Quality twice as fast as normal items
                if item.quality > 0: 
                    if item.name == "Conjured Mana Cake":
                        item.quality = item.quality - 1
            #“Aged Brie” actually increases in Quality the older it gets
            #“Backstage passes”, like aged brie, increases in Quality as it’s SellIn value approaches
            else:
                #The Quality of an item is never more than 50
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        #Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            #All items have a SellIn value which denotes the number of days we have to sell the item
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            #Once the sell by date has passed, Quality degrades twice as fast
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                        #“Conjured” items degrade in Quality twice as fast as normal items
                        if item.quality > 0: 
                            if item.name == "Conjured Mana Cake":
                                item.quality = item.quality - 1
                    #Quality drops to 0 after the concert
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)