from typing import Generator


def worker_fibo() -> Generator[None, int, None]:
    a = 0
    b = 1
    yield
    while True:
        a, b = b, a + b
        yield b

def worker_averager() -> Generator[float, float, None]:
    average = 0.0
    count = 1
    total = 0.0
    while True:
        value = yield average
        total += value
        average = total / count
        count += 1

def main():
    coroutine_fibo = worker_fibo()
    coroutine_averager = worker_averager()
    next(coroutine_fibo) # prime coroutine
    next(coroutine_averager) # prime coroutine

    fibo_val = 0
    average = 0.0
    target_fibo_val = 1000
    target_average = 100

    # "Event loop"
    while fibo_val < target_fibo_val and average < target_average:
        fibo_val = next(coroutine_fibo)
        print("fibo_val: ", fibo_val)
        average = coroutine_averager.send(fibo_val)
        print("average: ", average)

main()