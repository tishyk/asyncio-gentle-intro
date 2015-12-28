import asyncio

DELAY = 0.1

@asyncio.coroutine
def preheat_oven(target_temp):
    temp = 100
    while temp < target_temp:
        yield from asyncio.sleep(DELAY)
        temp += 100
        print("preheat:: temp is now {}".format(temp))

@asyncio.coroutine
def mix_ingredients(num):
    for i in range(num):
        yield from asyncio.sleep(DELAY)
        print("mix_ingredients:: mixing things {}".format(i))


@asyncio.coroutine
def bake_cake(minutes):
    for i in range(0, minutes, 4):
        yield from asyncio.sleep(DELAY)
        print("bake_cake:: baking for {} minutes".format(i))

@asyncio.coroutine
def make_frosting(minutes):
    for i in range(0, minutes, 4):
        yield from asyncio.sleep(DELAY)
        print("make_frosting:: making frosting for {} minutes".format(i))


def apply_frosting(minutes=4):
    import time
    for i in range(0, minutes, 2):
        time.sleep(DELAY)
        print("apply_frosting:: frosting for {} minutes".format(i))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    # Prep everything
    prep_tasks = [
        asyncio.async(preheat_oven(400)),
        asyncio.async(mix_ingredients(3))]
    loop.run_until_complete(asyncio.wait(prep_tasks))

    # Bake it and make frosting
    tasks = [
        asyncio.async(bake_cake(16)),
        asyncio.async(make_frosting(12))]
    loop.run_until_complete(asyncio.wait(tasks))

    apply_frosting()

    # TODO return values
    # TODO turning sync operations into asyncs
    # TODO queues, return values
