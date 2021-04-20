class tools(object):

    def __init__(self, name, country, price):
        self.name = name
        self.country = country
        self.price = price


first_tool = Tool("Drill", "Germany", 75000)
second_tool = Tool("Mallet", "USA", 5000)
third_tool = Tool("Chainsaw", "China", 15000)

print(second_tool.name)
print(first_tool.country)