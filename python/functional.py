#!/usr/bin/env python

# 'functional.py'.
# Chris Shiels.


def all(f, l):
  if len(l) == 0:
    return False
  elif len(l) == 1:
    return f(l[0])
  else:
    return f(l[0]) and all(f, l[1:])


def any(f, l):
  if len(l) == 0:
    return False
  elif len(l) == 1:
    return f(l[0])
  else:
    return f(l[0]) or any(f, l[1:])


def flatten(l):
  if l == []:
    return []
  elif type(l[0]) is list:
    return flatten(l[0]) + flatten(l[1:])
  else:
    return [ l[0] ] + flatten(l[1:])


def range(m, n = None, s = 1):
  def internal(start, stop, step):
    if step == 0 or \
       (step > 0 and start >= stop) or \
       (step < 0 and start <= stop):
      return []
    else:
      return [ start ] + internal(start + step, stop, step)
  if n is None:
    return internal(0, m, s)
  else:
    return internal(m, n, s)


def reduce(f, l, v = None):
  def internal(f, l, v):
    if l == []:
      return v
    else:
      return internal(f, l[1:], f(v, l[0]))
  if v is None:
    return internal(f, l[1:], l[0])
  else:
    return internal(f, l, v)


def scan(f, l, v):
  def internal(f, l, a):
    if l == []:
      return a
    else:
      return internal(f, l[1:], a + [f(a[-1], l[0])])
  return internal(f, l, [ v ])


def map(f, l):
  def accumulate(a, e):
    return a + [ f(e) ]
  return reduce(accumulate, l, [])


def filter(f, l):
  def accumulate(a, e):
    if f(e):
      return a + [ e ]
    else:
      return a
  return reduce(accumulate, l, [])


def partition(f, l):
  def accumulate(a, e):
    left, right = a
    if f(e):
      return [ left + [ e ], right ]
    else:
      return [ left, right + [ e ] ]
  return reduce(accumulate, l, [ [], [] ])


def split(f, l):
  def accumulate(a, e):
    if f(e):
      return a + [ [] ]
    else:
      return a[0:-1] + [ a[-1] + [ e ] ]

  def internal(e):
    return e != []
  return filter(internal, reduce(accumulate, l, [ [] ]))


def reverse(l):
  def accumulate(a, e):
    return [ e ] + a
  return reduce(accumulate, l, [])


def sort(f, l):
  if l == []:
    return []
  else:
    return sort(f, filter(lambda e: f(e, l[0]), l[1:])) + \
           [ l[0] ] + \
           sort(f, filter(lambda e: not f(e, l[0]), l[1:]))


def unique(l):
  def accumulate(a, e):
    if e in a:
      return a
    else:
      return a + [ e ]
  return reduce(accumulate, l, [])


def zip(l1, l2):
  if l1 == [] or l2 == []:
    return []
  else:
    return [ (l1[0], l2[0]) ] + zip(l1[1:], l2[1:])


def zipwith(f, l1, l2):
  if l1 == [] or l2 == []:
    return []
  else:
    return [ f(l1[0], l2[0]) ] + zipwith(f, l1[1:], l2[1:])


def permutations(l):
  if len(l) == 0:
    return []
  elif len(l) == 1:
    return [ l ]
  else:
    return reduce(lambda a, e1: a + map(lambda e2: [ e1 ] + e2,
                                        permutations(filter(lambda e3: e3 != e1,
                                                            l))),
                  l,
                  [])


def compose(f1, f2):
  def internal(v):
    return f2(f1(v))
  return internal


def pipe(l):
  def accumulate(a, e):
    return e(a)

  def internal(v):
    return reduce(accumulate, l, v)
  return internal


def pipe2(l):
  return reduce(compose, l)


def pipemaybe(l):
  def accumulate(a, e):
    if a != None:
      return e(a)
    else:
      return None

  def internal(v):
    return reduce(accumulate, l, v)
  return internal


def partial(f, *args1):
  def internal(*args2):
    return f(*(args1 + args2))
  return internal


def curry(f, arity = 0):
  arity = arity or f.__code__.co_argcount

  def internal(v):
    if arity == 1:
      return f(v)
    else:
      return curry(partial(f, v), arity - 1)
  return internal


def memoize(f):
  cache = {}

  def internal(*args):
    key = str(args)
    if not key in cache:
      cache[key] = f(*args)
    return cache[key]
  return internal


def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n - 1)


def fibonacci(n):
  if n <= 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


def memoizedfibonacci(n):
  def fibonacci(n):
    if n <= 1:
      return 1
    else:
      return fibonacci(n - 1) + fibonacci(n - 2)
  fibonacci = memoize(fibonacci)
  return fibonacci(n)


def primes(n):
  def sieve(l):
    if l == []:
      return []
    else:
      return [ l[0] ] + sieve(filter(lambda e: e % l[0] != 0, l[1:]))
  return sieve(range(2, n))


def ispalindrome(s):
  if len(s) == 0:
    return True
  elif s[0] != s[-1]:
    return False
  else:
    return ispalindrome(s[1:-1])
