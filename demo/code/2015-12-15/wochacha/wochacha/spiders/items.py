import scrapy


class MedicineItem(scrapy.Item):
    name = scrapy.Field()
    manufacturer = scrapy.Field()
    size = scrapy.Field()
    dosage = scrapy.Field()
    approval_number = scrapy.Field()
    barcode = scrapy.Field()