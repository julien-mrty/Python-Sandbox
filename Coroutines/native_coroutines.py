import asyncio

async def worker_fibo(queue):
    a = 0
    b = 1
    while True:
        await asyncio.sleep(1)
        a, b = b, a + b
        await queue.put(b)

async def worker_average(in_queue, out_queue):
    average = 0.0
    count = 1
    total = 0.0
    while True:
        value = await in_queue.get()
        total += value
        average = total / count
        count += 1
        await out_queue.put(average)


async def main():
    q_fibo = asyncio.Queue()
    q_in_avg = asyncio.Queue()
    q_out_avg = asyncio.Queue()
    task_fibo = asyncio.create_task(worker_fibo(q_fibo))
    task_avg = asyncio.create_task(worker_average(q_in_avg, q_out_avg))

    fibo_val = 0
    average = 0.0
    target_fibo_val = 1000
    target_average = 100

    # "Event loop"
    while fibo_val < target_fibo_val and average < target_average:
        fibo_val = await q_fibo.get()
        print("fibo_val: ", fibo_val)

        await q_in_avg.put(fibo_val)
        average = await q_out_avg.get()
        print("average: ", average)

    task_fibo.cancel()
    task_avg.cancel()
    await asyncio.gather(task_fibo, task_avg, return_exceptions=True)

asyncio.run(main())