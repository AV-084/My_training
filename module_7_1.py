from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')

class Shop(Product):
    def __init__(self, name, weight, category, __file_name='products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products  # Возвращаем прочитанное содержимое

    def add(self, *products):
        file = open(self.__file_name, 'r')
        existing_products = file.read()  # Читаем существующие продукты из файла
        file.close()

        for product in products:
            product_str = str(product) # Преобразуем продукт в строку
            if product_str in existing_products:
                print(f'Продукт {product_str} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{product_str}')
                file.close()


s1 = Shop('','', '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
#
print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

s1.get_products()
