""""""
"""
Classic coroutine: Control flow is manual.

caller -> send() -> coroutine -> yield -> caller

Explicitly resume execution with:
coroutine.send(value)


Native coroutine: Control flow is managed by an event loop.

task -> await -> event loop -> resume when ready

The coroutine suspends automatically until the awaited object is ready.
data = await socket.read()
"""

def g():
    yield

async def c():
    pass

print("Classic coroutines :", type(g()))
print("Native coroutines :", type(c()))

"""
Generators can act like coroutines, but native coroutines are a distinct type in Python's runtime.
Under the hood, native coroutines are still implemented using generators internally in CPython.
But they are treated differently by the interpreter and event loop.
"""