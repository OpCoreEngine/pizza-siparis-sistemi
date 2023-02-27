class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", 10.0)


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", 12.0)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Turk Pizza", 15.0)


class DominosPizza(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza", 18.0)
