# 'test_functional.py'.
# Chris Shiels.


import pytest


import functional


def test_all_recursive():
  assert functional.all_recursive(lambda e: e % 2 == 0,
                                  []) == \
         False
  assert functional.all_recursive(lambda e: e % 2 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.all_recursive(lambda e: e % 3 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         False
  with pytest.raises(RuntimeError):
    functional.all_recursive(lambda e: e, [ True ] * 1000)


def test_all_accumulator():
  assert functional.all_accumulator(lambda e: e % 2 == 0,
                                    []) == \
         False
  assert functional.all_accumulator(lambda e: e % 2 == 0,
                                    [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.all_accumulator(lambda e: e % 3 == 0,
                                    [ 2, 4, 6, 8, 10 ]) == \
         False
  assert functional.all_accumulator(lambda e: e,
                                    [ True ] * 1000) == \
         True


def test_all_callbacks():
  assert functional.all_callbacks(lambda e: e % 2 == 0,
                                  []) == \
         False
  assert functional.all_callbacks(lambda e: e % 2 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.all_callbacks(lambda e: e % 3 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         False
  assert functional.all_callbacks(lambda e: e,
                                  [ True ] * 1000) == \
         True


def test_any_recursive():
  assert functional.any_recursive(lambda e: e % 2 == 0,
                                  []) == \
         False
  assert functional.any_recursive(lambda e: e % 2 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.any_recursive(lambda e: e % 3 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         True
  with pytest.raises(RuntimeError):
    functional.any_recursive(lambda e: e, [ False ] * 1000)


def test_any_accumulator():
  assert functional.any_accumulator(lambda e: e % 2 == 0,
                                    []) == \
         False
  assert functional.any_accumulator(lambda e: e % 2 == 0,
                                    [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.any_accumulator(lambda e: e % 3 == 0,
                                    [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.any_accumulator(lambda e: e,
                                    [ True ] * 1000) == \
         True


def test_any_callbacks():
  assert functional.any_callbacks(lambda e: e % 2 == 0,
                                  []) == \
         False
  assert functional.any_callbacks(lambda e: e % 2 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.any_callbacks(lambda e: e % 3 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.any_callbacks(lambda e: e,
                                  [ True ] * 1000) == \
         True


def test_flatten_recursive():
  assert functional.flatten_recursive([]) == \
         []
  assert functional.flatten_recursive([ 1, 2, 3 ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_recursive([ [ 1, 2 ], 3 ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_recursive([ 1, [ 2, 3 ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_recursive([ 1, [ 2, [ 3 ] ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_recursive([ [ [ 1 ], [ 2 ], [ 3 ] ] ]) == \
         [ 1, 2, 3 ]
  with pytest.raises(RuntimeError):
    functional.flatten_recursive([ [ 1 ] ] * 1000)


def test_flatten_accumulator():
  assert functional.flatten_accumulator([]) == \
         []
  assert functional.flatten_accumulator([ 1, 2, 3 ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_accumulator([ [ 1, 2 ], 3 ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_accumulator([ 1, [ 2, 3 ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_accumulator([ 1, [ 2, [ 3 ] ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_accumulator([ [ [ 1 ], [ 2 ], [ 3 ] ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_accumulator([ [ 1 ] ] * 1000) == \
         [ 1 ] * 1000


def test_flatten_callbacks():
  assert functional.flatten_callbacks([]) == \
         []
  assert functional.flatten_callbacks([ 1, 2, 3 ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_callbacks([ [ 1, 2 ], 3 ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_callbacks([ 1, [ 2, 3 ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_callbacks([ 1, [ 2, [ 3 ] ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_callbacks([ [ [ 1 ], [ 2 ], [ 3 ] ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_callbacks([ [ 1 ] ] * 1000) == \
         [ 1 ] * 1000


def test_range():
  assert functional.range(0) == \
         []
  assert functional.range(10) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional.range(0, 10) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional.range(0, 10, 1) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional.range(0, 10, 2) == \
         [ 0, 2, 4, 6, 8 ]
  assert functional.range(0, 10, 3) == \
         [ 0, 3, 6, 9 ]
  assert functional.range(10, 0, -1) == \
         [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
  assert functional.range(1, 11) == \
         [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]


def test_reduce():
  assert functional.reduce(lambda a, e: a + e,
                            functional.range(1, 11), 0) == \
         55
  assert functional.reduce(lambda a, e: a + e,
                            functional.range(1, 11)) == \
         55
  assert functional.reduce(lambda a, e: a + e,
                            [ [ 1 ], [ 2, 3 ], [ 4, 5, 6 ] ]) == \
         [ 1, 2, 3, 4, 5, 6 ]
  assert functional.reduce(lambda a, e: a + len(e),
                            [ [ 1 ], [ 2, 3 ], [ 4, 5, 6 ] ],
                            0) == \
         6


def test_map():
  assert functional.map(lambda e: e * 2,
                        functional.range(1, 11)) == \
         [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 ]
  assert functional.map(lambda e: e,
                        [ [ 1 ], [ 2 ], [ 3 ] ]) == \
         [ [ 1 ], [ 2 ], [ 3 ] ]


def test_filter():
  assert functional.filter(lambda e: e % 2 == 0,
                           functional.range(1, 11)) == \
         [ 2, 4, 6, 8, 10 ]
  assert functional.filter(lambda e: e % 2 == 1,
                           functional.range(1, 11)) == \
         [ 1, 3, 5, 7, 9 ]
  assert functional.filter(lambda e: len(e) != 0,
                           [ [ 1 ], [], [ 2 ], [], [ 3 ] ]) == \
         [ [ 1 ], [ 2 ], [ 3 ] ]


def test_partition():
  assert functional.partition(lambda e: e % 3 == 0,
                              functional.range(1, 11)) == \
         [ [ 3, 6, 9 ], [ 1, 2, 4, 5, 7, 8, 10 ] ]
  assert functional.partition(lambda e: e % 3 != 0,
                              functional.range(1, 11)) == \
         [ [ 1, 2, 4, 5, 7, 8, 10 ], [ 3, 6, 9 ] ]
  assert functional.partition(lambda e: e == 0,
                              functional.range(1, 11)) == \
         [ [], [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] ]

  assert functional.partition(lambda e: len(e) > 1,
                              [ [ 1 ], [ 1, 2 ], [ 1, 2, 3 ] ]) == \
         [ [ [ 1, 2 ], [ 1, 2, 3 ] ], [ [ 1 ] ] ]


def test_split():
  assert functional.split(lambda e: e % 10 == 0,
                          []) == \
         []
  assert functional.split(lambda e: e % 1 == 0,
                          functional.range(1, 11)) == \
         []
  assert functional.split(lambda e: e % 2 == 0,
                          functional.range(1, 11)) == \
         [ [ 1 ], [ 3 ], [ 5 ], [ 7 ], [ 9 ] ]
  assert functional.split(lambda e: e % 3 == 0,
                          functional.range(1, 11)) == \
         [ [ 1, 2 ], [ 4, 5 ], [ 7, 8 ], [ 10 ] ]


def test_reverse():
  assert functional.reverse(functional.range(1, 11)) ==  \
         [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
  assert functional.reverse([ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ] ]) == \
         [ [ 5, 6 ], [ 3, 4 ], [ 1, 2 ] ]


def test_sort():
  assert functional.sort(lambda m, n: m <= n,
                         [1, 10, 2, 9, 3, 8, 4, 7, 5, 6 ]) == \
         functional.range(1, 11)
  assert functional.sort(lambda m, n: len(m) <= len(n),
                         [ [ 1, 2, 3], [ 1, 2 ], [ 1 ] ]) == \
         [ [ 1 ], [ 1, 2 ],  [ 1, 2, 3 ] ]


def test_unique():
  assert functional.unique([ 5, 1, 4, 2, 3, 3, 2, 4, 1, 5 ]) == \
         [ 5, 1, 4, 2, 3 ]


def test_zip():
  a = [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ] ]
  a1 = [ [ 1, 5 ],
         [ 2, 6 ],
         [ 3, 7 ],
         [ 4, 8 ] ]
  assert functional.zip(*a) == \
         a1
  assert functional.zip(*functional.zip(*a)) == a


def test_permutations():
  assert functional.permutations([]) == \
         []
  assert functional.permutations([ 1 ]) == \
         [ [ 1 ] ]
  assert functional.permutations([ 1, 2 ]) == \
         [ [ 1, 2 ], [ 2, 1 ] ]
  assert functional.permutations([ 1, 2, 3 ]) == \
         [ [ 1, 2, 3 ],
           [ 1, 3, 2 ],
           [ 2, 1, 3 ],
           [ 2, 3, 1 ],
           [ 3, 1, 2 ],
           [ 3, 2, 1 ] ]
  assert functional.permutations([ 1, 2, 3, 4 ]) == \
         [ [ 1, 2, 3, 4 ],
           [ 1, 2, 4, 3 ],
           [ 1, 3, 2, 4 ],
           [ 1, 3, 4, 2 ],
           [ 1, 4, 2, 3 ],
           [ 1, 4, 3, 2 ],
           [ 2, 1, 3, 4 ],
           [ 2, 1, 4, 3 ],
           [ 2, 3, 1, 4 ],
           [ 2, 3, 4, 1 ],
           [ 2, 4, 1, 3 ],
           [ 2, 4, 3, 1 ],
           [ 3, 1, 2, 4 ],
           [ 3, 1, 4, 2 ],
           [ 3, 2, 1, 4 ],
           [ 3, 2, 4, 1 ],
           [ 3, 4, 1, 2 ],
           [ 3, 4, 2, 1 ],
           [ 4, 1, 2, 3 ],
           [ 4, 1, 3, 2 ],
           [ 4, 2, 1, 3 ],
           [ 4, 2, 3, 1 ],
           [ 4, 3, 1, 2 ],
           [ 4, 3, 2, 1 ] ]


def test_compose():
  def valueadd1(v):
    return v + 1

  def valuemultiply2(v):
    return v * 2

  assert functional.compose(valueadd1, valuemultiply2)(1) == 4


def test_pipe():
  def valueadd1(v):
    return v + 1

  def valuemultiply2(v):
    return v * 2

  def listadd1(l):
    return functional.map(lambda e: e + 1, l)

  def listmultiply2(l):
    return functional.map(lambda e: e * 2, l)

  assert functional.pipe([ valueadd1,
                           valuemultiply2,
                           valueadd1 ])(1) == 5
  assert functional.pipe([ listadd1,
                           listmultiply2,
                           listadd1 ])(functional.range(1, 11)) == \
         [ 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 ]


def test_pipe2():
  def valueadd1(v):
    return v + 1

  def valuemultiply2(v):
    return v * 2

  def listadd1(l):
    return functional.map(lambda e: e + 1, l)

  def listmultiply2(l):
    return functional.map(lambda e: e * 2, l)

  assert functional.pipe2([ valueadd1,
                           valuemultiply2,
                           valueadd1 ])(1) == 5
  assert functional.pipe2([ listadd1,
                           listmultiply2,
                           listadd1 ])(functional.range(1, 11)) == \
         [ 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 ]


def test_pipemaybe():
  def valueadd1(v):
    return v + 1

  def valuenone(v):
    return None

  assert functional.pipemaybe([ valueadd1,
                                valueadd1,
                                valueadd1 ])(0) == 3
  assert functional.pipemaybe([ valueadd1,
                                valuenone,
                                valueadd1 ])(0) == None


def test_partial():
  def add(a, b):
    return a + b

  def add10(x):
    return add(x, 10)

  assert functional.map(add10,
                        functional.range(1, 11)) == \
         [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
  assert functional.map(functional.partial(add, 10),
                        functional.range(1, 11)) == \
         [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]


def test_curry():
  def args(*a):
    return a

  cargs = functional.curry(args, 5)
  cargsab = cargs('a')('b')
  assert cargsab('c')('d')('e') == ('a', 'b', 'c', 'd', 'e')
  assert cargsab('x')('y')('z') == ('a', 'b', 'x', 'y', 'z')
  assert cargsab('c')('d')('e') == ('a', 'b', 'c', 'd', 'e')
  assert cargsab('x')('y')('z') == ('a', 'b', 'x', 'y', 'z')


  def add(a, b):
    return a + b

  cadd = functional.curry(add)
  assert cadd(10)(5) == 15 and cadd(20)(5) == 25

  assert functional.map(functional.curry(add)(10),
                        functional.range(1, 11)) == \
         [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]


def test_factorial():
  assert functional.map(functional.factorial, functional.range(1, 11)) == \
         [ 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800 ]


def test_fibonacci():
  assert functional.map(functional.fibonacci, functional.range(1, 11)) == \
         [ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ]


def test_memoizedfibonacci():
  assert functional.memoizedfibonacci(50) == \
         20365011074


def test_primes():
  assert functional.primes(20) == \
         [ 2, 3, 5, 7, 11, 13, 17, 19 ]


def test_ispalindrome():
  assert functional.ispalindrome('tattarrattat') == \
         True
