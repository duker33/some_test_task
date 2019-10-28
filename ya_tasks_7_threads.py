import asyncio
import random
import typing
from itertools import zip_longest


async def send_items(items: list):
    assert isinstance(items, list), type(items)
    # асинхронная отправка массива элементов куда-то
    # await http_post(URL, json.dumps(items))
    await fake_send(items)
    

async def send_items_threads(items: list, *, threads: int = 2, limit: int = 10):
    for cluster in split_longest(items, threads*limit):
        await asyncio.gather(*[
            send_items(list(filter(None, container)))
            for container in split_longest(cluster, limit)
        ])


def split_longest(items: list, limit: int, fillvalue=None) -> typing.List[list]:
    aligned_items = items + [fillvalue]*((limit - len(items) % limit) % limit)
    N = len(aligned_items)
    assert N % limit == 0
    return [
        aligned_items[left:right]
        for left, right in zip(range(0, N, limit), range(limit, N+1, limit))
    ]


# ---- TESTS ----
assert split_longest([], limit=3) == []
assert split_longest([1, 2], limit=2) == [[1, 2]], split_longest([1, 2], limit=2)
assert split_longest([1, 2, 3, 4], limit=2) == [[1, 2], [3, 4]], split_longest([1, 2, 3, 4], limit=2)
assert split_longest([1, 2, 3, 4], limit=3) == [[1, 2, 3], [4, None, None]], split_longest([1, 2, 3, 4], limit=3)


received = []


async def fake_send(items: list):
    global received
    await asyncio.sleep(random.randint(1, 5) / 10)
    print('in fake send', items)
    received += items


def test_threads(items: list, *, threads: int, limit: int):
    global received
    received = []
    asyncio.run(send_items_threads(items, threads=threads, limit=limit))
    assert set(items) == set(received), received
    assert len(items) == len(received), (len(items), len(received))


test_threads([1, 2, 3, 4], threads=2, limit=2)
test_threads([1, 2, 3, 4], threads=2, limit=3)
