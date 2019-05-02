# functional/python

Implementations of common functional programming functions in Python:
all, any, flatten, range, reduce, map, filter, partition, permutations,
split, reverse, sort, unique, zip, compose, pipe, pipemaybe, partial,
curry and memoize.

    host$ virtualenv virtualenv

    host$ . virtualenv/bin/activate

    (virtualenv) host$ pip install -r requirements.txt

    (virtualenv) host$ pytest -v --cov tests/
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.15, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- /home/chris/github.com/functional/python/virtualenv/bin/python2
    cachedir: .pytest_cache
    rootdir: /home/chris/github.com/functional/python
    plugins: cov-2.6.1
    collected 25 items

    tests/test_functional.py::test_all PASSED                                [  4%]
    tests/test_functional.py::test_any PASSED                                [  8%]
    tests/test_functional.py::test_flatten PASSED                            [ 12%]
    tests/test_functional.py::test_range PASSED                              [ 16%]
    tests/test_functional.py::test_reduce PASSED                             [ 20%]
    tests/test_functional.py::test_map PASSED                                [ 24%]
    tests/test_functional.py::test_filter PASSED                             [ 28%]
    tests/test_functional.py::test_partition PASSED                          [ 32%]
    tests/test_functional.py::test_split PASSED                              [ 36%]
    tests/test_functional.py::test_reverse PASSED                            [ 40%]
    tests/test_functional.py::test_sort PASSED                               [ 44%]
    tests/test_functional.py::test_unique PASSED                             [ 48%]
    tests/test_functional.py::test_zip PASSED                                [ 52%]
    tests/test_functional.py::test_permutations PASSED                       [ 56%]
    tests/test_functional.py::test_compose PASSED                            [ 60%]
    tests/test_functional.py::test_pipe PASSED                               [ 64%]
    tests/test_functional.py::test_pipe2 PASSED                              [ 68%]
    tests/test_functional.py::test_pipemaybe PASSED                          [ 72%]
    tests/test_functional.py::test_partial PASSED                            [ 76%]
    tests/test_functional.py::test_curry PASSED                              [ 80%]
    tests/test_functional.py::test_factorial PASSED                          [ 84%]
    tests/test_functional.py::test_fibonacci PASSED                          [ 88%]
    tests/test_functional.py::test_memoizedfibonacci PASSED                  [ 92%]
    tests/test_functional.py::test_primes PASSED                             [ 96%]
    tests/test_functional.py::test_ispalindrome PASSED                       [100%]

    ---------- coverage: platform linux2, python 2.7.15-final-0 ----------
    Name                       Stmts   Miss  Cover
    ----------------------------------------------
    tests/__init__.py              0      0   100%
    tests/test_functional.py     132      0   100%
    ----------------------------------------------
    TOTAL                        132      0   100%


    ========================== 25 passed in 0.07 seconds ===========================
