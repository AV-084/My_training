class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):

    def __init__(self, name, weight, category, __file_name = 'product.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'r')
        existing_product = file.read()
        file.close()

        for product in products:
            product_str = str(product)
            if product_str in existing_product:
                print(f'Продукт {product_str} уже имеется в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{product_str}\n')
                file.close()

s1 = Shop('', '', '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())



