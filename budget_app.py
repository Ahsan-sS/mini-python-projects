#Python budget app - -
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = f"{item['description'][:23]:<23}"
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

def create_spend_chart(categories):
    # Calculate spending for each category (withdrawals only)
    withdrawals = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        withdrawals.append(spent)
    
    total_spent = sum(withdrawals)
    
    # Calculate percentages rounded down to nearest 10
    percentages = []
    for spent in withdrawals:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentages.append(int((spent / total_spent) * 100) // 10 * 10)

    # Build the chart line by line from 100 down to 0
    chart = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for pct in percentages:
            chart += "o  " if pct >= level else "   "
        chart += "\n"

    # Add horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Add vertical category names
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]

    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += f"{name[i]}  "
        if i < max_len - 1:
            chart += "\n"

    return chart

# Example usage:
food = Category("Food")
entertainment = Category("Entertainment")
food.deposit(900, "groceries")
food.deposit(125, "restaurant")
entertainment.deposit(49.99, "movies")

# Test Category object
print(food)
print(entertainment)

# Test __str__ method and transfer
food.transfer(200, entertainment)
print(food)
print(entertainment)

# Test create_spend_chart
categories = [food, entertainment]
print(create_spend_chart(categories))
