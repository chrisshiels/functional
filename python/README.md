# functional/python

Implementations of common functional programming functions in Python:
range, reduce, map, filter, partition, reverse, sort, unique, zip, compose,
pipe, partial, curry and memoize.

    host$ virtualenv virtualenv
    
    host$ . virtualenv/bin/activate
    
    (virtualenv) host$ pip install -r requirements.txt
    
    (virtualenv) host$ pytest -v
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.13, pytest-3.2.1, py-1.4.34, pluggy-0.4.0 -- /home/chris/chris/functional/python/virtualenv/bin/python2
    cachedir: .cache
    rootdir: /home/chris/chris/functional/python, inifile:
    collected 19 items
    
    test_functional.py::test_range PASSED
    test_functional.py::test_reduce PASSED
    test_functional.py::test_map PASSED
    test_functional.py::test_filter PASSED
    test_functional.py::test_partition PASSED
    test_functional.py::test_reverse PASSED
    test_functional.py::test_sort PASSED
    test_functional.py::test_unique PASSED
    test_functional.py::test_zip PASSED
    test_functional.py::test_compose PASSED
    test_functional.py::test_pipe PASSED
    test_functional.py::test_pipe2 PASSED
    test_functional.py::test_partial PASSED
    test_functional.py::test_curry PASSED
    test_functional.py::test_factorial PASSED
    test_functional.py::test_fibonacci PASSED
    test_functional.py::test_memoizedfibonacci PASSED
    test_functional.py::test_primes PASSED
    test_functional.py::test_ispalindrome PASSED
    
    ========================== 19 passed in 0.03 seconds ===========================
