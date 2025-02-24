class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name  # название продукта
        self.weight = weight  # общий вес товара
        self.category = category  # категория товара


    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'


    def get_products(self):
        file = open(self.__file_name, 'r')
        return file.read()


    def add(self, *products):
        existing_products = self.get_products()  # Получаем текущие товары

        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)
                # Проверяем, есть ли продукт в существующих
                if product_str in existing_products:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(product_str + '\n')  # Записываем новый продукт.


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
