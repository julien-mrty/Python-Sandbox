""""""
"""
Should impl two coroutines that need to wait for data, giving control back to the event loop while waiting.

A coroutine is not like a CPU thread that is literally executing at the same instant as another thread. It is more like:

run until you need to wait

save your state

let someone else run

come back later

That is why asyncio is great for I/O-bound work, but not for speeding up pure CPU-heavy computation.

it is not async compute in the sense of parallel arithmetic. It is asynchronous concurrency: lots of tasks making progress over time, without blocking each other.
"""