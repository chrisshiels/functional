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


def zip(*args):
  def accumulateheads(a, e):
    return a + [ e[0] ]
  def accumulatetails(a, e):
    return a + [ e[1:] ]
  args = list(args)
  if args[0] == []:
    return []
  return [ reduce(accumulateheads, args, []) ] + \
             zip(*reduce(accumulatetails, args, []))


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


def compose(f, g):
  def internal(v):
    return f(g(v))
  return internal


def pipe(l):
  def accumulate(a, e):
    return e(a)

  def internal(v):
    return reduce(accumulate, l, v)
  return internal


def pipe2(l):
  return reduce(compose, reverse(l))


def pipemaybe(l):
  def accumulate(a, e):
    if a != None:
      return e(a)
    else:
      return None

  def internal(v):
    return reduce(accumulate, l, v)
  return internal


def partial(f, *args):
  args1 = args

  def internal(*args):
    return f(*(args1 + args))
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
    if key in cache:
      return cache[key]
    else:
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
  def internal(f, n):
    if n <= 1:
      return 1
    else:
      return f(f, n - 1) + f(f, n - 2)
  f = memoize(internal)
  return f(f, n)


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
