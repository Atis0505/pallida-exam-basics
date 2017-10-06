# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candie's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
#
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.
# we can create lollipops and candies store them in the CandyShop's storage
# If we create a candie or lollipop the CandyShop's sugar amount gets reduced by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"
class Sweet:
    def __init__(self, sweet_type):
        self.sweet_type = sweet_type
        if self.sweet_type == "candy":
            self.price = 20
            self.sugar = 10
        elif self.sweet_type == "lollipop":
            self.price = 10
            self.sugar = 5


class CandyShop:
    def __init__(self, amount_of_sugar):
        self.amount_of_sugar = amount_of_sugar
        self.money
        self.lollipops_and_candies = []
        self.income = 0


    def create_sweets(self, kind_of_sweet):
        sweet = Sweet(kind_of_sweet)
        self.lollipops_and_candies.append(sweet)
        self.amount_of_sugar -= sweet.price


    def raise_prices(self, precentage):
        for sweet in self.lollipops_and_candies:
            sweet.price += sweet.price+precentage

    
    def sell(self, sweet_type, number_of_amount):
        for index, sweet in enumerate(self.lollipops_and_candies):
            if sweet.sweet_type == sweet_type and index <= number_of_amount:
                del self.lollipops_and_candies[index]
                self.income += sweet.price


    def buy_sugar(self, amount_of_sugar):
        self.income -= amount_of_sugar/10

    



candy_shop = CandyShop(300)
candy_shop.create_sweets("candy")
candy_shop.create_sweets("candy")
candy_shop.create_sweets("lollipop")
candy_shop.create_sweets("lollipop")
print(candy_shop)
# Should print out:
# Invetory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr
candy_shop.sell("candy", 1)
print(candy_shop
# Should print out:
# "Invetory: 1 candies, 2 lollipops, Income:20, Sugar: 285gr"
candy_shop.raise_prices(5)
candy_shop.sell("lollipop", 1)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:35, Sugar: 285gr"
candy_shop.buy_sugar(300)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:5, Sugar: 315gr"
