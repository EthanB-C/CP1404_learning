# products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
#
# on_sale_products = [product for product in products if product[2] is True]
# print(on_sale_products)

"""
1. creating class (new type)
2. defining class method
3. self refers to this instance of the class
4. new class is a specialised version of Kivy's App class (inheritance)
5. create new object of type HeloowWorld
6. call method "run" of new object (defined by Kivy

Remember

Classes create objects

Method is essentially a function within a class, and can be called

self is a reference to a particular instance of class, e.g that particular use of the class

entering a class into a new class type creates a version of that existing class, with some tweaks

by calling a class you can call particular methods of that class e.g HelloWorld().run() refers to the method in
HelloWorld() called 'run()'
"""


class Product:
    def __init__(self, product_name, price, on_sale):
        self.product_name = product_name
        self.price = price
        self.on_sale = on_sale


computer = Product('computer', 300, True)
phone = Product('phone', 200, False)
plant = Product('plant', 20, True)

products = [computer, phone, plant]

# on_sale_products =
print([spec_product for spec_product in products if spec_product.on_sale is True])
# print(on_sale_products)
print([product.product_name for product in products])
