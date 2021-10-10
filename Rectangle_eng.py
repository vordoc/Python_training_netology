def rectangle_area(length, width):
    area = length * width
    return area


def rectangle_perimeter(length, width):
    perimeter = (length + width) * 2
    return perimeter


if __name__ == '__main__':
    print('Commands available: p - perimeter, a - area')
    command = input('Enter a command: ')
    if command == 'a':
        print(
            f"Rectangle area is: {rectangle_area(int(input('Enter rectangle length: ')), (int(input('Enter rectangle width: '))))}")
    elif command == 'p':
        print(
            f"Rectangle perimeter is: {rectangle_perimeter(int(input('Enter rectangle length: ')), (int(input('Enter rectangle width: '))))}")
    else:
        print('invalid command!')
