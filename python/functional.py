#!/usr/bin/env python

# 'functional.py'.
# Chris Shiels.


def _range(n, m = 0):
  if n == m:
    return []
  else:
    return _range(n - 1, m) + [ n - 1 ]


def _reverse(l):
  if l == []:
    return []
  else:
    return _reverse(l[1:]) + [ l[0] ]


def _reduce(f, l, v):
  if l == []:
    return v
  else:
    return _reduce(f, l[1:], f(v, l[0]))


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


def _partial(f, *args):
  args1 = args

  def internal(*args):
    return f(*(args1 + args))
  return internal


def _curry(f, arity):
  def internal(v):
    if arity == 1:
      return f(v)
    else:
      return _curry(_partial(f, v), arity - 1)
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


def primes(n):
  def notdivisibleby(y, x):
    return x % y != 0

  def sieve(f, l):
    if l == []:
      return []
    else:
      return [ l[0] ] + sieve(f, _filter(_partial(f, l[0]), l[1:]))
  return sieve(notdivisibleby, _range(n, 2))
