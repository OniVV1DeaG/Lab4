from itertools import islice

MIN_FUNC_RANGE = 0
MAX_FUNC_RANGE = 100
STEP = 0.01
COUNT = 50

def calculate_function(min_func : int = MIN_FUNC_RANGE, max_func : int = MAX_FUNC_RANGE,
                      step : float = STEP, count : int = COUNT):
    results = list(islice((float(0.5*i*step - 2) for i in range(min_func, int(max_func//step))), count))
    return results

def print_results(results : list) -> None:
    print(results)

def process():
    print_results(calculate_function())

if __name__ == "__main__":
    process()