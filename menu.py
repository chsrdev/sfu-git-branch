from matrix import Matrix

matrix: Matrix


def main_menu():
    while True:
            action = input("1. Ввод размера массива\n"
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


def create_menu():
    while True:
        action = input("Создание массива\n"
                       "1. Вручную\n"
                       "2. Автоматически\n"
                       "3. Назад\n"
                       "Выберите действие: ")

        match action:
            case "1":
                ...
            case "2":
                ...
            case "3":
                break
            case _:
                print("Введено некорректное действие")


def functions_menu():
    while True:
        action = input("Выполнение функций\n"
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
        