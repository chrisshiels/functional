#!/usr/bin/env python

# 'test.py'.
# Chris Shiels.


import atexit


tests = []

def test(f):
  global tests

  def complete():
    for test in tests:
      print '%s:  %s' % ( test[0], 'ok' if test[1]() else 'fail' )

  if len(tests) == 0:
    atexit.register(complete)
  tests = tests + [ [ f.__name__, f ] ]

  def internal(*args, **kwargs):
    return f(*args, **kwargs)

  return internal


import functional


@test
def test_range1():
  return functional._range(10) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]


@test
def test_range2():
  return functional._range(11, 1) == \
         [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]


@test
def test_reverse():
  return functional._reverse(functional._range(11, 1)) ==  \
         [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]


@test
def test_reduce():
  return functional._reduce(lambda a, e: a + e,
                            functional._range(11, 1), 0) == \
         55


@test
def test_map():
  return functional._map(lambda e: e * 2,
                         functional._range(11, 1)) == \
         [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 ]


@test
def test_filter_even():
  return functional._filter(lambda e: e % 2 == 0,
                            functional._range(11, 1)) == \
         [ 2, 4, 6, 8, 10 ]


@test
def test_filter_odd():
  return functional._filter(lambda e: e % 2 == 1,
                            functional._range(11, 1)) == \
         [ 1, 3, 5, 7, 9 ]


@test
def test_sort():
  return functional._sort(lambda m, n: m <= n,
                          [1, 10, 2, 9, 3, 8, 4, 7, 5, 6 ]) == \
         functional._range(11, 1)


@test
def test_unique():
  return functional._unique([ 5, 1, 4, 2, 3, 3, 2, 4, 1, 5 ]) == \
         [ 5, 1, 4, 2, 3 ]


@test
def test_zip1():
  a = [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ] ]
  a1 = [ [ 1, 5 ],
         [ 2, 6 ],
         [ 3, 7 ],
         [ 4, 8 ] ]
  return functional._zip(*a) == \
        a1


@test
def test_zip2():
  a = [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ] ]
  return functional._zip(*functional._zip(*a)) == a


@test
def test_compose():
  def valueadd1(v):
    return v + 1

  def valuemultiply2(v):
    return v * 2

  return functional._compose(valueadd1, valuemultiply2)(1) == 3


@test
def test_pipe1():
  def valueadd1(v):
    return v + 1

  def valuemultiply2(v):
    return v * 2

  return functional._pipe([ valueadd1,
                            valuemultiply2,
                            valueadd1 ])(1) == \
         5


@test
def test_pipe2():
  def listadd1(l):
    return functional._map(lambda e: e + 1, l)

  def listmultiply2(l):
    return functional._map(lambda e: e * 2, l)

  return functional._pipe([ listadd1,
                            listmultiply2,
                            listadd1 ])(functional._range(11, 1)) == \
         [ 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 ]


@test
def test_partial():
  def add(a, b):
    return a + b

  def add10(x):
    return add(x, 10)

  return functional._map(add10,
                         functional._range(11, 1)) == \
         [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ] and \
         functional._map(functional._partial(add, 10),
                         functional._range(11, 1)) == \
         [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]


@test
def test_curry1():
  def args(*a):
    return a

  cargs = functional._curry(args, 5)
  cargsab = cargs('a')('b')
  return cargsab('c')('d')('e') == ('a', 'b', 'c', 'd', 'e') and \
         cargsab('x')('y')('z') == ('a', 'b', 'x', 'y', 'z') and \
         cargsab('c')('d')('e') == ('a', 'b', 'c', 'd', 'e') and \
         cargsab('x')('y')('z') == ('a', 'b', 'x', 'y', 'z')


@test
def test_curry2():
  def add(a, b):
    return a + b

  cadd = functional._curry(add, 2)
  return cadd(10)(5) == 15 and cadd(20)(5) == 25


@test
def test_curry3():
  def add(a, b):
    return a + b

  return functional._map(functional._curry(add, 2)(10),
                         functional._range(11, 1)) == \
         [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]


@test
def test_factorial():
  return functional._map(functional.factorial, functional._range(11, 1)) == \
         [ 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800 ]


@test
def test_fibonacci():
  return functional._map(functional.fibonacci, functional._range(11, 1)) == \
         [ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ]


@test
def test_memoizedfibonacci():
  return functional.memoizedfibonacci(50) == \
         20365011074


@test
def test_primes():
  return functional.primes(20) == \
         [ 2, 3, 5, 7, 11, 13, 17, 19 ]


@test
def test_ispalindrome():
  return functional.ispalindrome('tattarrattat') == \
         True
