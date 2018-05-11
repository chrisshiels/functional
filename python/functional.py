#!/usr/bin/env python

# 'functional.py'.
# Chris Shiels.


def _all(f, l):
  if len(l) == 0:
    return False
  elif len(l) == 1:
    return f(l[0])
  else:
    return f(l[0]) and _all(f, l[1:])


def _any(f, l):
  if len(l) == 0:
    return False
  elif len(l) == 1:
    return f(l[0])
  else:
    return f(l[0]) or _any(f, l[1:])


def _flatten(l):
  if l == []:
    return []
  elif type(l[0]) is list:
    return _flatten(l[0]) + _flatten(l[1:])
  else:
    return [ l[0] ] + _flatten(l[1:])


def _range(m, n = None, s = 1):
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


def _reduce(f, l, v = None):
  def internal(f, l, v):
    if l == []:
      return v
    else:
      return internal(f, l[1:], f(v, l[0]))
  if v is None:
    return internal(f, l[1:], l[0])
  else:
    return internal(f, l, v)


def _map(f, l):
  def accumulate(a, e):
    return a + [ f(e) ]
  return _reduce(accumulate, l, [])


def _filter(f, l):
  def accumulate(a, e):
    if f(e):
      return a + [ e ]
    else:
      return a
  return _reduce(accumulate, l, [])


def _partition(f, l):
  def accumulate(a, e):
    left, right = a
    if f(e):
      return [ left + [ e ], right ]
    else:
      return [ left, right + [ e ] ]
  return _reduce(accumulate, l, [ [], [] ])


def _split(f, l):
  def accumulate(a, e):
    if f(e):
      return a + [ [] ]
    else:
      return a[0:-1] + [ a[-1] + [ e ] ]

  def internal(e):
    return e != []
  return _filter(internal, _reduce(accumulate, l, [ [] ]))


def _reverse(l):
  def accumulate(a, e):
    return [ e ] + a
  return _reduce(accumulate, l, [])


def _sort(f, l):
  if l == []:
    return []
  else:
    return _sort(f, _filter(lambda e: f(e, l[0]), l[1:])) + \
           [ l[0] ] + \
           _sort(f, _filter(lambda e: not f(e, l[0]), l[1:]))


def _unique(l):
  def accumulate(a, e):
    if e in a:
      return a
    else:
      return a + [ e ]
  return _reduce(accumulate, l, [])


def _zip(*args):
  def accumulateheads(a, e):
    return a + [ e[0] ]
  def accumulatetails(a, e):
    return a + [ e[1:] ]
  args = list(args)
  if args[0] == []:
    return []
  return [ _reduce(accumulateheads, args, []) ] + _zip(*_reduce(accumulatetails, args, []))


def _compose(f, g):
  def internal(v):
    return f(g(v))
  return internal


def _pipe(l):
  def accumulate(a, e):
    return e(a)

  def internal(v):
    return _reduce(accumulate, l, v)
  return internal


def _pipe2(l):
  return _reduce(_compose, _reverse(l))


def _pipemaybe(l):
  def accumulate(a, e):
    if a != None:
      return e(a)
    else:
      return None

  def internal(v):
    return _reduce(accumulate, l, v)
  return internal


def _partial(f, *args):
  args1 = args

  def internal(*args):
    return f(*(args1 + args))
  return internal


def _curry(f, arity = 0):
  arity = arity or f.__code__.co_argcount

  def internal(v):
    if arity == 1:
      return f(v)
    else:
      return _curry(_partial(f, v), arity - 1)
  return internal


def _memoize(f):
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
  f = _memoize(internal)
  return f(f, n)


def primes(n):
  def notdivisibleby(y, x):
    return x % y != 0

  def sieve(f, l):
    if l == []:
      return []
    else:
      return [ l[0] ] + sieve(f, _filter(_partial(f, l[0]), l[1:]))
  return sieve(notdivisibleby, _range(2, n))


def ispalindrome(s):
  if len(s) == 0:
    return True
  elif s[0] != s[-1]:
    return False
  else:
    return ispalindrome(s[1:-1])
