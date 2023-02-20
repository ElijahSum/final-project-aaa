import random
from typing import (
    Callable,
    Optional
)
import click
from pizza import (
    BasePizza,
    Margherita,
    PepperoniPizza,
    Hawaiian
)

PIZZA_SIZES = BasePizza.SIZES
MENU = (
    *[Margherita(size=size) for size in PIZZA_SIZES],
    *[PepperoniPizza(size=size) for size in PIZZA_SIZES],
    *[Hawaiian(size=size) for size in PIZZA_SIZES]
)
MAX_DELIVERY_TIME = 4
MAX_PICKUP_TIME = 2
DEFAULT_BAKING_TIME = 10


@click.group()
def cli():
    """
    A plug
    :return: None
    """


def log(format_str: str = '') -> Callable:
    """
    Decorator which prints the function name and its return value
    :param format_str: str
    :return: Calable
    """
    def outer_wrapper(func: Callable) -> Callable:
        nonlocal format_str
        if not format_str:
            format_str = func.__name__ + ' - {} seconds!'

        def inner_wrapper(*args, **kwargs) -> str:
            result = func(*args, **kwargs)
            nonlocal format_str
            return format_str.format(result)

        return inner_wrapper

    return outer_wrapper


@log('🍴 Приготовили за {} с!')
def bake(pizza: BasePizza) -> int:
    """
    :param pizza: BasePizza
    :return baking_time (in seconds): int
    """
    return DEFAULT_BAKING_TIME + len(pizza.content)


@log('🚗 Доставили за {} с!')
def deliver() -> int:
    """
    :return deliver_time (in seconds): int
    """
    return random.randint(0, MAX_DELIVERY_TIME)


@log('🏠 Забрали за {} с!')
def pickup() -> int:
    """
    :return pickup_time (in seconds): int
    """
    return random.randint(0, MAX_PICKUP_TIME)


def get_pizza_by_name(pizza_name: str, pizza_size: str) -> Optional[BasePizza]:
    """
    Factory method which returns BasePizza instance
    :param pizza_name: str
    :param pizza_size: str
    :return: Optional[BasePizza]
    """
    for dish in MENU:
        if isinstance(dish, BasePizza) and dish.name == pizza_name \
                and dish.size == pizza_size:
            return dish

    return None


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--size', default=BasePizza.SIZES[0])
@click.argument('pizza_name', nargs=1)
def order(pizza_name: str, delivery: bool, size: str):
    """
    API function which prints information about an order
    :param pizza_name: str
    :param delivery: bool
    :param size: str
    :return: None
    """
    pizza = get_pizza_by_name(pizza_name, size)

    if pizza is None:
        raise ValueError(
            f'Pizza with name={pizza_name} and size={size} is not available'
        )

    print(bake(pizza))

    if delivery:
        print(deliver())
    else:
        print(pickup())


@cli.command()
def menu():
    """
    API function which prints the menu
    :return: None
    """
    for dish in MENU:
        print('-', dish)


if __name__ == '__main__':
    cli()