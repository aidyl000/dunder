class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        # return self.name + '$' + str(self.price)
        return f'{self.name} ${self.price}' # string formatting

    def __repr__(self):
        return f'<Product({self.name}, {self.price})>'

    def __add__(self, other):
        if isinstance(other, str): # other是否屬於str類別
            self.name += other
        if isinstance(other,Product):
            return [self, other]
    def __mul__(self, other):
        re = []
        if isinstance(other, int):
            for _ in range(other):
                re.append(self)
        return re

    def print_name(self):
        print(self.name)

p1 = Product('珍珠奶茶', 60)
p2 = Product('磅蛋糕', 50)
# p + '白玉'
# p1 + p2

# print(repr(p))

class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def __getitem__(self, key):
        return self.products[key]

s = ShoppingCart([p1, p2])


if __name__ == '__main__':
    print(p1 * 5)
    print(s[1])
    