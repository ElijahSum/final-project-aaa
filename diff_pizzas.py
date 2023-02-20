class Pizza_base:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return self.name


class TomatoSauce(Pizza_base):
    def __init__(self):
        super().__init__('tomato sauce')


class Mozzarella(Pizza_base):
    def __init__(self):
        super().__init__('mozzarella')


class Tomato(Pizza_base):
    def __init__(self):
        super().__init__('tomatoes')


class Pepperoni(Pizza_base):
    def __init__(self):
        super().__init__('pepperoni')


class Chicken(Pizza_base):
    def __init__(self):
        super().__init__('chicken')


class Pineapple(Pizza_base):
    def __init__(self):
        super().__init__('pineapples')
