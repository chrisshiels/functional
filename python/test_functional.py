# 'test_functional.py'.
# Chris Shiels.


import functional


def test_range():
  assert functional._range(10) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional._range(11, 1) == \
         [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]


def test_reduce():
  assert functional._reduce(lambda a, e: a + e,
                            functional._range(11, 1), 0) == \
         55


def test_map():
  assert functional._map(lambda e: e * 2,
                         functional._range(11, 1)) == \
         [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 ]


def test_filter():
  assert functional._filter(lambda e: e % 2 == 0,
                            functional._range(11, 1)) == \
         [ 2, 4, 6, 8, 10 ]
  assert functional._filter(lambda e: e % 2 == 1,
                            functional._range(11, 1)) == \
         [ 1, 3, 5, 7, 9 ]


def test_partition():
  assert functional._partition(lambda e: e % 3 == 0,
                               functional._range(11, 1)) == \
         [ [ 3, 6, 9 ], [ 1, 2, 4, 5, 7, 8, 10 ] ]
  assert functional._partition(lambda e: e % 3 != 0,
                               functional._range(11, 1)) == \
         [ [ 1, 2, 4, 5, 7, 8, 10 ], [ 3, 6, 9 ] ]
  assert functional._partition(lambda e: e == 0,
                               functional._range(11, 1)) == \
         [ [], [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] ]


def test_reverse():
  assert functional._reverse(functional._range(11, 1)) ==  \
         [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]


def test_sort():
  assert functional._sort(lambda m, n: m <= n,
                          [1, 10, 2, 9, 3, 8, 4, 7, 5, 6 ]) == \
         functional._range(11, 1)


def test_unique():
  assert functional._unique([ 5, 1, 4, 2, 3, 3, 2, 4, 1, 5 ]) == \
         [ 5, 1, 4, 2, 3 ]


def test_zip():
  a = [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ] ]
  a1 = [ [ 1, 5 ],
         [ 2, 6 ],
         [ 3, 7 ],
         [ 4, 8 ] ]
  assert functional._zip(*a) == \
         a1
  assert functional._zip(*functional._zip(*a)) == a


def test_compose():
  def valueadd1(v):
    return v + 1

  def valuemultiply2(v):
    return v * 2

  assert functional._compose(valueadd1, valuemultiply2)(1) == 3


def test_pipe():
  def valueadd1(v):
    return v + 1

  def valuemultiply2(v):
    return v * 2

  def listadd1(l):
    return functional._map(lambda e: e + 1, l)

  def listmultiply2(l):
    return functional._map(lambda e: e * 2, l)

  assert functional._pipe([ valueadd1,
                            valuemultiply2,
                            valueadd1 ])(1) == 5
  assert functional._pipe([ listadd1,
                            listmultiply2,
                            listadd1 ])(functional._range(11, 1)) == \
         [ 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 ]


def test_partial():
  def add(a, b):
    return a + b

  def add10(x):
    return add(x, 10)

  assert functional._map(add10,
                         functional._range(11, 1)) == \
         [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
  assert functional._map(functional._partial(add, 10),
                         functional._range(11, 1)) == \
         [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]


def test_curry():
  def args(*a):
    return a

  cargs = functional._curry(args, 5)
  cargsab = cargs('a')('b')
  assert cargsab('c')('d')('e') == ('a', 'b', 'c', 'd', 'e')
  assert cargsab('x')('y')('z') == ('a', 'b', 'x', 'y', 'z')
  assert cargsab('c')('d')('e') == ('a', 'b', 'c', 'd', 'e')
  assert cargsab('x')('y')('z') == ('a', 'b', 'x', 'y', 'z')


  def add(a, b):
    return a + b

  cadd = functional._curry(add, 2)
  assert cadd(10)(5) == 15 and cadd(20)(5) == 25
  assert functional._map(functional._curry(add, 2)(10),
                         functional._range(11, 1)) == \
         [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]


def test_factorial():
  assert functional._map(functional.factorial, functional._range(11, 1)) == \
         [ 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800 ]


def test_fibonacci():
  assert functional._map(functional.fibonacci, functional._range(11, 1)) == \
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
