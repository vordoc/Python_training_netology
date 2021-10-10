def rectangle_area(length, width):
    area = length * width
    return area


def rectangle_perimeter(length, width):
    perimeter = (length + width) * 2
    return perimeter


if __name__ == '__main__':
    print('Доступные команды: p - периметр, a - площадь')
    command = input('Введите команду: ')
    if command == 'a':
        print(
            f"Площадь прямоугольника равна: {rectangle_area(int(input('Введите длину прямоугольника: ')), (int(input('Введите ширину прямоугольника: '))))}")
    elif command == 'p':
        print(
            f"Периметр прямоугольника равен: {rectangle_perimeter(int(input('Введите длину прямоугольника: ')), (int(input('Введите ширину прямоугольника: '))))}")
    else:
        print('Неверная команда!')
