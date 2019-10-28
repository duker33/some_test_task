import asyncio


async def foobar(*args, **kwargs):
    await asyncio.sleep(1.0)
    return random.choice(TEST_RESULTS)


# ---- The second approach ----
async def foobar_single(*args, _foobar_result=[], **kwargs):
    if not _foobar_result:
        _foobar_result.append(await foobar(*args, **kwargs))
    return _foobar_result[0]


# ---- Test for the both approaches ----
TEST_RESULTS = [None, 1, 2, 3, [1, 2], object()]  # None, basic types, some mutables builtin types, object
TEST_COUNT = 10  # much more then possible results set of foobar func

async def run_test():
    results = [res for res in await asyncio.gather(
        *(foobar_single() for _ in range(TEST_COUNT))
    )]
    assert all(results[0] == r for r in results)

asyncio.run(run_test())
