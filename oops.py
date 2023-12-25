import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate(self):
        return self.price * self.quantity

    def discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantatiate_csv(cls):
        with open('items.csv') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}',{self.price}, {self.quantity})"


Item.instantatiate_csv()
print(Item.all)
# for instance in Item.all:
#     print(instance.name)
# print(Item.all)
# item1.discount()
# print(item1.price)
# item2.pay_rate = 0.7
# item2.discount()
# print(item2.price)
