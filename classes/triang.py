from random import choice

MIN = 2
MAX = 20
COUNT = 20

def generate_sides():
    for i in range(MIN, MAX):
        for j in range (MIN, MAX):
            for y in range (MIN, MAX):
                is_triangle = ((i+j) > y) and ((y+j) > i) and ((i+y) > j)
                yield i, j, y, is_triangle


def create_sides_array() -> list:
    temp = generate_sides()
    array = [next(temp) for i in range (COUNT)]
    return array

def print_array(array : list) -> None:
    print(array)

def process():
    print_array(create_sides_array())

if __name__ == "__main__":
    process()
