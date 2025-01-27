"""Program will ask calculate quantity of tea bags, number of treats, and expected cost of a tea party based on user's responded number of guests"""

__author__ = "730567639"


def main_planner(guests: int) -> None:
    """Serves as a main function and entrypoint of program"""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculates number of tea bags"""
    return people * 2


def treats(people: int) -> int:
    """Returns number of treats needed"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates total cost of tea bags and treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
