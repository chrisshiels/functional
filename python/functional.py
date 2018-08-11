#!/usr/bin/env python

# 'functional.py'.
# Chris Shiels.


def trampoline(f):
  def internal(*args):
    v = f(*args)
    while callable(v):
      v = v()
    return v
  return internal


def all_recursive(f, l):
  def all(f, l):
    if len(l) == 0:
      return False
    elif len(l) == 1:
      return f(l[0])
    else:
      return f(l[0]) and all(f, l[1:])
  return all(f, l)


def all_accumulator(f, l):
  def all(f, l, a = True):
    if len(l) == 0:
      return False
    elif len(l) == 1:
      return a
    else:
      return lambda: all(f, l[1:], f(l[0]) and a)
  return trampoline(all)(f, l)


def all_callbacks(f, l):
  def all(f, l, c = lambda v: v):
    if len(l) == 0:
      return c(False)
    elif len(l) == 1:
      return c(f(l[0]))
    else:
      return lambda: all(f, l[1:], lambda v: lambda: c(f(l[0]) and v))
  return trampoline(all)(f, l)


all = all_callbacks


def any_recursive(f, l):
  def any(f, l):
    if len(l) == 0:
      return False
    elif len(l) == 1:
      return f(l[0])
    else:
      return f(l[0]) or any(f, l[1:])
  return any(f, l)


def any_accumulator(f, l):
  def any(f, l, a = True):
    if len(l) == 0:
      return False
    elif len(l) == 1:
      return a
    else:
      return lambda: any(f, l[1:], f(l[0]) or a)
  return trampoline(any)(f, l)


def any_callbacks(f, l):
  def any(f, l, c = lambda v: v):
    if len(l) == 0:
      return c(False)
    elif len(l) == 1:
      return c(f(l[0]))
    else:
      return lambda: any(f, l[1:], lambda v: lambda: c(f(l[0]) or v))
  return trampoline(any)(f, l)


any = any_callbacks


def flatten_recursive(l):
  def flatten(l):
    if l == []:
      return []
    elif type(l[0]) is list:
      return flatten(l[0]) + flatten(l[1:])
    else:
      return [ l[0] ] + flatten(l[1:])
  return flatten(l)


def flatten_accumulator(l):
  def flatten(l, a = []):
    if l == []:
      return a
    elif type(l[0]) is list:
      return lambda: flatten(l[0] + l[1:], a)
    else:
      return lambda: flatten(l[1:], a + [ l[0] ])
  return trampoline(flatten)(l)


def flatten_callbacks(l):
  def flatten(l, c = lambda v: v):
    if l == []:
      return c([])
    elif type(l[0]) is list:
      return lambda: flatten(l[0] + l[1:], lambda v: lambda: c(v))
    else:
      return lambda: flatten(l[1:], lambda v: lambda: c([ l[0] ] + v))
  return trampoline(flatten)(l)


flatten = flatten_callbacks


def range_recursive(m, n = None, s = 1):
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
  return range(m, n, s)


def range_accumulator(m, n = None, s = 1):
  def range(m, n = None, s = 1):
    def internal(start, stop, step, a = []):
      if step == 0 or \
         (step > 0 and start >= stop) or \
         (step < 0 and start <= stop):
        return a
      else:
        return lambda: internal(start + step, stop, step, a + [ start ])
    if n is None:
      return internal(0, m, s)
    else:
      return internal(m, n, s)
  return trampoline(range)(m, n, s)


def range_callbacks(m, n = None, s = 1):
  def range(m, n = None, s = 1):
    def internal(start, stop, step, c = lambda v: v):
      if step == 0 or \
         (step > 0 and start >= stop) or \
         (step < 0 and start <= stop):
        return c([])
      else:
        return lambda: internal(start + step,
                                stop,
                                step,
                                lambda v: lambda: c([ start ] + v))
    if n is None:
      return internal(0, m, s)
    else:
      return internal(m, n, s)
  return trampoline(range)(m, n, s)


range = range_callbacks


def reduce_accumulator(f, l, v = None):
  def reduce(f, l, v = None):
    def internal(f, l, v):
      if l == []:
        return v
      else:
        return lambda: internal(f, l[1:], f(v, l[0]))
    if v is None:
      return internal(f, l[1:], l[0])
    else:
      return internal(f, l, v)
  return trampoline(reduce)(f, l, v)


reduce = reduce_accumulator


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


def sort_recursive(f, l):
  def sort(f, l):
    if l == []:
      return []
    else:
      return sort(f, filter(lambda e: f(e, l[0]), l[1:])) + \
             [ l[0] ] + \
             sort(f, filter(lambda e: not f(e, l[0]), l[1:]))
  return sort(f, l)


def sort_callbacks(f, l):
  def sort(f, l, c = lambda v: v):
    if l == []:
      return c([])
    else:
      return lambda: \
               sort(f,
                    filter(lambda e: f(e, l[0]), l[1:]),
                    lambda v1:
                      lambda:
                        sort(f,
                             filter(lambda e: not f(e, l[0]), l[1:]),
                             lambda v2:
                               lambda: c(v1 + [ l[0] ] + v2)))
  return trampoline(sort)(f, l)


sort = sort_callbacks


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


# Note pipe2 is not compatible with the trampoline implementation of reduce.
#def pipe2(l):
#  return reduce(compose, l)


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
