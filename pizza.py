from typing import Optional, Sequence
from diff_pizzas import (
    Pizza_base,
    TomatoSauce,
    Mozzarella,
    Tomato,
    Pepperoni,
    Chicken,
    Pineapple
)


class BasePizza:
    """BasePizza"""
    SIZES = ('L', 'XL')

    def __init__(self, name: str, size: str, content: Sequence[Pizza_base]):
        self.size = size
        self.content = content
        self.name = name

    @property
    def size(self) -> str:
        """
        Pizza size
        :return size: str
        """
        return self._size

    @size.setter
    def size(self, new_size: str):
        if new_size not in self.SIZES:
            raise ValueError(f'Pizza size {new_size} is not supported')

        self._size = new_size

    @property
    def content(self) -> Sequence[Pizza_base]:
        """
        Pizza ingredients
        :return content: Iterable[Ingredient]
        """
        return self._content

    @content.setter
    def content(self, new_content: Sequence[Pizza_base]):
        self._content = new_content

    @property
    def name(self) -> str:
        """
        Pizza name
        :return name: str
        """
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    def __dict__(self):
        return {self.name: self.content}

    def __eq__(self, other):
        return self.size == other.size and \
               sorted(self.content) == sorted(other.content)

    def __repr__(self):
        return self.name + ' ' + self.size + ': ' + \
               ', '.join(str(x) for x in self.content)


class PizzaEmojiMixin:
    """Mixin for displaying pizza emoji"""
    DEFAULT_EMOJI = '😬'

    def __init__(self, emoji: Optional[str]):
        self.emoji = emoji

    @property
    def emoji(self):
        """
        Get emoji
        :return emoji: str
        """
        if self._emoji is None:
            return self.DEFAULT_EMOJI

        return self._emoji

    @emoji.setter
    def emoji(self, new_emoji: Optional[str]):
        self._emoji = new_emoji

    def __repr__(self):
        repr_str = super().__repr__()
        sep_ind = repr_str.find(':')

        return repr_str[:sep_ind] + ' ' + self.emoji + repr_str[sep_ind:]


class Margherita(PizzaEmojiMixin, BasePizza):
    """Pizza Margherita"""
    def __init__(self, size: str = BasePizza.SIZES[0]):
        content = [TomatoSauce(), Mozzarella(), Tomato()]
        BasePizza.__init__(self, 'margherita', size, content)
        PizzaEmojiMixin.__init__(self, '🧀')


class PepperoniPizza(PizzaEmojiMixin, BasePizza):
    """Pizza Pepperoni"""
    def __init__(self, size: str = BasePizza.SIZES[0]):
        content = [TomatoSauce(), Mozzarella(), Pepperoni()]
        BasePizza.__init__(self, 'pepperoni', size, content)
        PizzaEmojiMixin.__init__(self, '🍕')


class Hawaiian(PizzaEmojiMixin, BasePizza):
    """Pizza hawaiian"""
    def __init__(self, size: str = BasePizza.SIZES[0]):
        content = [TomatoSauce(), Mozzarella(), Chicken(), Pineapple()]
        BasePizza.__init__(self, 'hawaiian', size, content)
        PizzaEmojiMixin.__init__(self, '🍍')


if __name__ == '__main__':
    print(Margherita('XL'))
