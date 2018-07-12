# functional/python

Implementations of common functional programming functions in Python:
all, any, flatten, range, reduce, map, filter, partition, permutations,
split, reverse, sort, unique, zip, compose, pipe, pipemaybe, partial,
curry and memoize.

    host$ virtualenv virtualenv

    host$ . virtualenv/bin/activate

    (virtualenv) host$ pip install -r requirements.txt

    (virtualenv) host$ pytest -v
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.15, pytest-3.6.3, py-1.5.4, pluggy-0.6.0 -- /home/chris/github.com/functional/python/virtualenv/bin/python2
    cachedir: .pytest_cache
    rootdir: /home/chris/github.com/functional/python, inifile:
    collected 25 items

    test_functional.py::test_all PASSED                                      [  4%]
    test_functional.py::test_any PASSED                                      [  8%]
    test_functional.py::test_flatten PASSED                                  [ 12%]
    test_functional.py::test_range PASSED                                    [ 16%]
    test_functional.py::test_reduce PASSED                                   [ 20%]
    test_functional.py::test_map PASSED                                      [ 24%]
    test_functional.py::test_filter PASSED                                   [ 28%]
    test_functional.py::test_partition PASSED                                [ 32%]
    test_functional.py::test_split PASSED                                    [ 36%]
    test_functional.py::test_reverse PASSED                                  [ 40%]
    test_functional.py::test_sort PASSED                                     [ 44%]
    test_functional.py::test_unique PASSED                                   [ 48%]
    test_functional.py::test_zip PASSED                                      [ 52%]
    test_functional.py::test_permutations PASSED                             [ 56%]
    test_functional.py::test_compose PASSED                                  [ 60%]
    test_functional.py::test_pipe PASSED                                     [ 64%]
    test_functional.py::test_pipe2 PASSED                                    [ 68%]
    test_functional.py::test_pipemaybe PASSED                                [ 72%]
    test_functional.py::test_partial PASSED                                  [ 76%]
    test_functional.py::test_curry PASSED                                    [ 80%]
    test_functional.py::test_factorial PASSED                                [ 84%]
    test_functional.py::test_fibonacci PASSED                                [ 88%]
    test_functional.py::test_memoizedfibonacci PASSED                        [ 92%]
    test_functional.py::test_primes PASSED                                   [ 96%]
    test_functional.py::test_ispalindrome PASSED                             [100%]

    ========================== 25 passed in 0.03 seconds ===========================
