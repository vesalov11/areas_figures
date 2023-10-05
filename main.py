import math


def main():
    print("Изберете фигура:")
    print("1. Квадрат")
    print("2. Правоъгълник")
    print("3. Триъгълник")
    print("4. Кръг")

    choice = int(input("Въведете номера на фигурата: "))

    if choice == 1:
        side = float(input("Въведете страната на квадрата: "))
        area = calculate_square_area(side)
        print(f"Лицето на квадрата е {area}")
    elif choice == 2:
        length = float(input("Въведете дължината на правоъгълника: "))
        width = float(input("Въведете ширината на правоъгълника: "))
        area = calculate_rectangle_area(length, width)
        print(f"Лицето на правоъгълника е {area}")
    elif choice == 3:
        base = float(input("Въведете дължината на основата на триъгълника: "))
        height = float(input("Въведете височината на триъгълника: "))
        area = calculate_triangle_area(base, height)
        print(f"Лицето на триъгълника е {area}")
    elif choice == 4:
        radius = float(input("Въведете радиуса на кръга: "))
        area = calculate_circle_area(radius)
        print(f"Лицето на кръга е {area}")
    else:
        print("Грешен избор!")


def calculate_square_area(side):
    return side ** 2


def calculate_rectangle_area(length, width):
    return length * width


def calculate_triangle_area(base, height):
    return 0.5 * base * height


def calculate_circle_area(radius):
    return math.pi * radius ** 2


if __name__ == "__main__":
    main()
