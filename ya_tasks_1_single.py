import random
from hypothesis import given, strategies as st


def foobar(*args, **kwargs):
    ...
    return random.choice(TEST_RESULTS)


def foobar_single(*args, **kwargs):
    if not hasattr(foobar, 'single_result'):
        foobar.single_result = foobar(*args, **kwargs)
    return foobar.single_result


TEST_RESULTS = [None, 1, 2, 3, [1, 2], object()]  # None, basic types, some mutables builtin types, object
TEST_COUNT = 1000  # much more then possible results set of foobar func

single_value = foobar_single()
assert all((single_value == foobar_single() for _ in range(TEST_COUNT)))
