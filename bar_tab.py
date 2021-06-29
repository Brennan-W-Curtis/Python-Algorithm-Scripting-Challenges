class Tab:
    menu = {
        "wine": 5,
        "beer": 3,
        "soft_drink": 2,
        "chicken": 10,
        "beef": 15,
        "vegetables": 12,
        "dessert": 6
    } 

    def __init__(self):
        self.total = 0
        self.items = []
    
    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]
    
    def print_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = self.total + tax + service
        
        for item in self.items:
            print(f"{item:20} ${self.menu[item]}")

        print(f"{'Total':20} ${total:.2f}")

# To execute program
# 1. Start by typing "python" into your terminal
# 2. Then "from bar_tab import tab"
# 3. Declare a new table "table1 = Tab()"
# 4. Add menu items "table1.add("beer")
# 5. Determine what the tax and service charges are
# 6. Lastly, provide these values as arguments "table1.print_bill(10, 10)" 
