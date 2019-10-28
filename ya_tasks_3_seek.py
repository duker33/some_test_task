import typing

# O(len(db)*len(pattern)) complexity is the best i can propose
def seek(db: typing.List[str], pattern: typing.List[str]) -> typing.Union[int, None]:
    if not pattern:
        return 0
    step = len(pattern)
    for pos in range(len(db)):
        if db[pos:pos+step] == pattern:
            return pos

# ---- TESTS ----
assert 0 == seek(list('abcd'), list('abc'))
assert None == seek(list('abcd'), list('ba'))
assert 1 == seek(list('zabcd'), list('abc')), seek(list('zabcd'), list('abc'))
assert 1 == seek(list('aaab'), list('aab'))
assert 3 == seek(list('abcd'), list('d'))

# it's 0 but not None since `'' in ''` leads to `True`
assert 0 == seek(list(''), list(''))
assert None == seek(list(''), list('abc'))  
assert 0 == seek(list('abc'), list(''))

assert None == seek(['ab', 'cd'], ['abc', 'd'])
assert None == seek(['ab', 'cd'], ['abcd', ''])
assert 0 == seek(['ab', 'cd'], ['ab', 'cd'])
assert 1 == seek(['yz', 'ab', 'cd'], ['ab', 'cd'])
assert None == seek([''], ['', ''])
assert 0 == seek(['', ''], [''])
assert 0 == seek(['', ''], ['', ''])
assert 0 == seek([''], [''])

assert 2 == seek(list('Hello, world'), list('l'))
