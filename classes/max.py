COUNT = 4

def my_input() -> list:
    input_array = [int(x) for x in input("Введите список: ").split()]
    return input_array

def calculate_max(input_num : list) -> list:
    nums = set(input_num)
    nums = sorted(nums,reverse = True)[:4]
    return nums

def print_result(numbers : list) -> None:
    print(numbers)

def process():
    first = my_input()
    print(calculate_max(first))

if __name__ == "__main__":
    process()