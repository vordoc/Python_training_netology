from typing import Any
import datetime


class StackItem:

    def __init__(self, value: Any, prev_stack_item: 'StackItem' = None):
        self.value = value
        self.prev_stack_item = prev_stack_item


class Stack:

    def __init__(self):
        self.tail: StackItem = None

    def append(self, value: Any):
        new_stack_item = StackItem(value, self.tail)
        self.tail = new_stack_item

    def pop(self) -> Any:
        value = self.tail.value
        self.tail = self.tail.prev_stack_item
        return value


class StackIterable(Stack):

    def __iter__(self):
        self.cursor = StackItem(None, self.tail)
        return self

    def __next__(self):
        if self.cursor.prev_stack_item is None:
            raise StopIteration
        value = self.cursor.prev_stack_item.value
        self.cursor = self.cursor.prev_stack_item
        return value


# my_stack = Stack()
# my_stack.append(2)
# my_stack.append(8)
# my_stack.append(False)
# print(my_stack.pop())
# print(my_stack.pop())
# print(my_stack.pop())

# my_stack = StackIterable()
# my_stack.append(5)
# my_stack.append(True)
# my_stack.append('bla')
#
# for item in my_stack:
#     print(item)


def my_range(start: datetime.date, end: datetime.date):
    cursor = start
    while cursor != end:
        yield cursor
        cursor += datetime.timedelta(days=1)


for item in my_range(
    datetime.date(2021, 6, 1),
    datetime.date(2021, 6, 10)
):
    print(item)



my_list = [2, 4, 5]
# my_list_sq = []
# for item in my_list:
#     my_list_sq.append(item*item)
#
# print(my_list_sq)

my_list_square = [item * item for item in my_list]
# print(my_list_square)


my_list_square = (item * item for item in my_list) #генератор
for item in my_list_square:
    print(item)

















