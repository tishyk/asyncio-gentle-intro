# Baking a cake: Why we need asyncronous code

This is a basic analogy that explains why we need asyncio. Consider the process of baking a cake:

Before you bake a cake, you need to preheat the oven

```python
def preheat_oven(target_temp):
    temp = 100
    while temp < target_temp:
        time.sleep(1)  # simulates the length of the task 
        temp += 100
        print("preheat:: temp is now {}".format(temp))
```

And you also need to mix the ingredients to make the batter. 

```python
def mix_ingredients(num):
    for i in range(num):
        time.sleep(1)
        print("mix_ingredients:: mixing things {}".format(i))
```

You *could* perform these tasks syncronously, first preheating the oven to the desired 
temperature, then mixing the ingredients.

```python
preheat_oven(400)
mix_ingredients(3)
```

Which results in the following output. Note how the mixing doesn't begin until the oven is completely preheated. 

```
preheat:: temp is now 200
preheat:: temp is now 300
preheat:: temp is now 400
mix_ingredients:: mixing things 0
mix_ingredients:: mixing things 1
mix_ingredients:: mixing things 2
```

Is there any reason we need to wait for the oven to preheat before start mixing ingredients? Of course not. 
In asyncronous code, we would say that preheat_oven is a **blocking** operation since nothing can
be done until it's complete.

We could easily start mixing ingredients while the oven was preheating. This is the essence of asyncronous code;
when one operation need not block the other, we can do something else while we wait.

Note that this is different from computation parallelism. TODO.

## Async made simple(ish)

But take a look at the async version of our cake example and see how similar they are:

```python
@asyncio.coroutine
def preheat_oven(target_temp):
    temp = 100
    while temp < target_temp:
        yield from asyncio.sleep(1)
        temp += 100
        print("preheat:: temp is now {}".format(temp))

@asyncio.coroutine
def mix_ingredients(num):
    for i in range(num):
        yield from asyncio.sleep(1)
        print("mix_ingredients:: mixing things {}".format(i))
```

You'll notice two main differences compared to the syncronous code:

* We use the `@asyncio.coroutine` decorator. This declares the function as a **coroutine** -
    code that can be executed in a non-blocking way.
* We use the `yield from asyncio.sleep(1)` to avoid blocking. Instead of executing the sleep
    right then and there, we create a a promise of work to be done and yield control 
    back so that other code can keep running.

In order to use the async code, you need to create an **event loop**. The event loop is a common pattern:
* wait for events
* start responding to the event (the response is completed *sometime in the future*)
* return control to event loop quickly and wait for the next event

If you're familiar with callbacks in Javascript, that is the JS approach. `yield from` provides a much cleaner abstraction allowing you to write functions which look *almost* like regular linear functions without callbacks. 

The response to the event should take place asyncronously, otherwie it will block the event loop which is considered a *bad thing*. In async programming, we should always return control to the main event loop
as soon as possible. Any lengthy computations (our `preheat_oven` and `mix_ingredients` coroutines for example) can be handled without holding up the show.


```python
loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        preheat_oven(400),
        mix_ingredients(3)))
```

Here we start an event loop and tell it to run until it has gathered the results of the two funtions. 
A little more involved than just calling the functions but the result is worth the effort; we can
now execute both tasks concurrently:

```
preheat:: temp is now 200
mix_ingredients:: mixing things 0
preheat:: temp is now 300
mix_ingredients:: mixing things 1
preheat:: temp is now 400
mix_ingredients:: mixing things 2
```

I won't lie and say asyncio removes all complexity from async code. Asyncio is still more complex than
its syncronous equivalent. But it opens the door to so many things...
