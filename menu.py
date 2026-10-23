from matrix import Matrix

matrix: Matrix = None


def main_menu():
    global matrix 

    while True:
        action = input("\n1. Ввод размера массива\n"
                    "2. Создание массива\n"
                    "3. Просмотр созданного массива\n"
                    "4. Выполнение функций\n"
                    "5. Выход\n"
                    "Выберите действие: ")

        match action:
            case "1":
                try:
                    width = int(input("Ширина двумерного массива: "))
                    height = int(input("Высота двумерного массива: "))
                    if width < 0 or height < 0:
                        print("Ширина и высота массива не могут быть меньше нуля.")
                except ValueError as e:
                    print(f"Ошибка: {e}")

                matrix = Matrix(width, height)
            case "2":
                create_menu()
            case "3":
                ...
            case "4":
                functions_menu()
            case "5":
                break
            case _:
                print("Введено некорректное действие")


def input_array():
    global matrix

    for i in range(matrix.get_height()):
        for j in range(matrix.get_width()):
            while True:
                try:
                    num = int(input(f"{i} строчка, {j} столбец | Число: "))
                    matrix.set_number(i, j, num)
                    break
                except (ValueError, IndexError) as e:
                    print(f"Ошибка: {e}")


def create_menu():
    global matrix

    if not matrix:
        print("\nСначала укажите размер матрицы")
        return
    
    while True:
        action = input("\nСоздание массива\n"
                       "1. Вручную\n"
                       "2. Автоматически\n"
                       "3. Назад\n"
                       "Выберите действие: ")

        match action:
            case "1":
                input_array()
                print("Массив заполнен")
            case "2":
                matrix.fill_random()
                print("Массив заполнен")
            case "3":
                break
            case _:
                print("Введено некорректное действие")


def functions_menu():
    while True:
        action = input("\nВыполнение функций\n"
                       "a. Функция 16\n"
                       "Вывести номера тех строк массива, в которых есть хотя бы один элемент, равный 10.\n"
                       "b. Функция 18\n"
                       "Поменять местами первую и последнюю строку.\n"
                       "c. Функция 19\n"
                       "Поменять местами первый и последний столбец.\n"
                       "d. Функция 22\n"
                       "Найти сумму всех четных элементов двумерного массива целых чисел.\n"
                       "e. Функция 28\n"
                       "Найти все неповторяющиеся элементы двумерного массива целых чисел.\n"
                       "f. Назад\n"
                       "Выберите действие: ")

        match action:
            case "a":
                ...
            case "b":
                ...
            case "c":
                ...
            case "d":
                ...
            case "e":
                ...
            case "f":
                break
            case _:
                print("Введено некорректное действие")
        