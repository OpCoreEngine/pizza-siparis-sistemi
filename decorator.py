from pizza import Pizza


class Decorator(Pizza):
    def __init__(self, pizza, description, cost):
        super().__init__(pizza.get_description(), pizza.get_cost())
        self.component = pizza
        self.description = description
        self.cost = cost

    def get_cost(self):
        return self.component.get_cost() + self.cost

    def get_description(self):
        return self.component.get_description() + ', ' + self.description


class Olives(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Olives", 2.0)


class Mushrooms(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Mushrooms", 1.5)


class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Goat Cheese", 3.0)


class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Meat", 2.5)


class Onions(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Onions", 1.0)


class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Corn", 1.0)
