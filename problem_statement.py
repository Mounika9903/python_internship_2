# from abc import ABC, abstractmethod
# class AbstractItem(ABC):
#     @abstractmethod
#     def calculate_total_price(self):
#         pass
# class Item(AbstractItem):
#     def __init__(self, name, quantity, price_per_unit, tax_rate):
#         self.__name = name
#         self.quantity = quantity
#         self.price_per_unit = price_per_unit
#         self.tax_rate = tax_rate
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#     def calculate_total_price(self):
#         return self.quantity * self.price_per_unit * (1 + self.tax_rate / 100)
# class Bill:
#     def __init__(self):
#         self.items = []
#     def add_item(self, name, quantity, price_per_unit, tax_rate):
#         if quantity > 0 and price_per_unit > 0:
#             self.items.append(Item(name, quantity, price_per_unit, tax_rate))
#         else:
#             print("Quantity and price must be positive.")
#     def remove_item(self, name):
#         for item in self.items:
#             if item.name == name:
#                 self.items.remove(item)
#                 return
#         print(f"Item '{name}' not found in the bill.")
#     def generate_bill(self):
#         total_amount = 0
#         print("---------- Bill ----------")
#         for item in self.items:
#             item_total = item.calculate_total_price()
#             total_amount += item_total
#             print(f"{item.name} - Total: {item_total:.2f}")
#         print(f"\nTotal Bill Amount: {total_amount:.2f}")
#         print("--------------------------")
#         return total_amount
    
#     def __add__(self, other):
#         combined_bill = Bill()
#         combined_bill.items = self.items + other.items
#         return combined_bill
# class DiscountBill(Bill):
#     def __init__(self, discount_rate):
#         super().__init__()
#         self.discount_rate = discount_rate
    
#     def generate_bill(self):
#         total_amount = super().generate_bill()
#         discount = total_amount * (self.discount_rate / 100)
#         final_amount = total_amount - discount
#         print(f"Discount Applied: -{discount:.2f}")
#         print(f"Final Amount Payable: {final_amount:.2f}")
#         print("--------------------------")
# bill1 = Bill()
# bill1.add_item("Apple", 3, 20, 2)
# bill1.add_item("Banana", 6, 10, 5)
# bill1.generate_bill()

# bill2 = Bill()
# bill2.add_item("Milk", 2, 50, 5)
# bill2.add_item("Bread", 1, 30, 2)
# bill3 = bill1 + bill2  
# bill3.generate_bill()

# discounted_bill = DiscountBill(10)
# discounted_bill.add_item("Orange", 5, 15, 3)
# discounted_bill.generate_bill()

from abc import ABC, abstractmethod

class AbstractItem(ABC):
    @abstractmethod
    def calculate_total_price(self):
        pass

class Item(AbstractItem):
    def __init__(self, name, quantity, price_per_unit, tax_rate):
        self.__name = name
        self.__quantity = quantity
        self.__price_per_unit = price_per_unit
        self.__tax_rate = tax_rate / 100  

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def calculate_total_price(self):
        price_without_tax = self.__quantity * self.__price_per_unit
        tax_amount = price_without_tax * self.__tax_rate
        total_price = price_without_tax + tax_amount
        return total_price

class Bill:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, quantity, price_per_unit, tax_rate):
        if quantity <= 0 or price_per_unit <= 0:
            print(f"Error: Invalid input for {name}. Quantity and price must be positive.")
            return
        item = Item(name, quantity, price_per_unit, tax_rate)
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item.get_name() == name:
                self.items.remove(item)
                print(f"Removed {name} from the bill.")
                return
        print(f"Item {name} not found in the bill.")

    def generate_bill(self):
        print("\n---------- Bill ----------")
        total_bill = 0
        for item in self.items:
            item_total = item.calculate_total_price()
            total_bill += item_total
            print(f"{item.get_name()} - Total: {item_total:.2f}")
        print(f"\nTotal Bill Amount: {total_bill:.2f}")
        print("--------------------------")
        return total_bill

    def __add__(self, other):
        new_bill = Bill()
        new_bill.items = self.items + other.items
        return new_bill

class DiscountBill(Bill):
    def __init__(self, discount_rate):
        super().__init__()
        self.discount_rate = discount_rate / 100  

    def generate_bill(self):
        total_bill = super().generate_bill()
        discount_amount = total_bill * self.discount_rate
        final_amount = total_bill - discount_amount
        print(f"Discount Applied: -{discount_amount:.2f}")
        print(f"Final Amount Payable: {final_amount:.2f}")
        print("--------------------------")

bill1 = Bill()
bill1.add_item("Apple", 3, 20, 2)   
bill1.add_item("Banana", 6, 10, 5)
bill1.generate_bill()

bill2 = Bill()
bill2.add_item("Milk", 2, 50, 5)
bill2.add_item("Bread", 1, 30, 2)

bill1= bill1 + bill2
bill1.generate_bill()

discounted_bill = DiscountBill(10)
discounted_bill.add_item("Orange", 5, 15, 3)
discounted_bill.generate_bill()

