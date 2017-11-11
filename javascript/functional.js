#!/usr/bin/env node

// 'functional.js'.
// Chris Shiels.


'use strict';


const _flatten = function(l) {
  if (l.length === 0)
    return [];
  else if (l[0] instanceof Array)
    return _flatten(l[0]).concat(_flatten(l.slice(1)));
  else
    return [ l[0] ].concat(_flatten(l.slice(1)));
}


const _range = function(m, n = null, s = 1) {
  const internal = function(start, stop, step) {
    if (step === 0 ||
        (step > 0 && start >= stop) ||
        (step < 0 && start <= stop))
      return [];
    else
      return [ start ].concat(internal(start + step, stop, step));
  }
  if (n === null)
    return internal(0, m, s);
  else
    return internal(m, n, s);
}


const _reduce = function(f, l, v = null) {
  const internal = function(f, l, v) {
    if (l.length === 0)
      return v;
    else
      return internal(f, l.slice(1), f(v, l[0]));
  }
  if (v === null)
    return internal(f, l.slice(1), l[0]);
  else
    return internal(f, l, v);
}


const _map = function(f, l) {
  const accumulate = function(a, e) {
    return a.concat(f(e));
  }
  return _reduce(accumulate, l, []);
}


const _filter = function(f, l) {
  const accumulate = function(a, e) {
    if (f(e))
      return a.concat(e);
    else
      return a;
  }
  return _reduce(accumulate, l, []);
}


const _partition = function(f, l) {
  const accumulate = function(a, e) {
    let left, right;
    [ left, right ] = a;
    if (f(e))
      return [ left.concat(e), right ];
    else
      return [ left, right.concat(e) ];
  }
  return _reduce(accumulate, l, [ [], [] ]);
}


const _reverse = function(l) {
  const accumulate = function(a, e) {
    return [ e ].concat(a);
  }
  return _reduce(accumulate, l, []);
}


const _sort = function(f, l) {
  if (l.length === 0)
    return [];
  return _sort(f, _filter((e) => { return f(e, l[0]); }, l.slice(1)))
         .concat(l[0])
         .concat(_sort(f, _filter((e) => { return !f(e, l[0]); }, l.slice(1))));
}


const _unique = function(l) {
  const accumulate = function(a, e) {
    if (a.includes(e))
      return a;
    else
      return a.concat(e);
  }
  return _reduce(accumulate, l, []);
}


const _zip = function(...args) {
  const accumulateheads = function(a, e) {
    return a.concat(e[0]);
  }
  const accumulatetails = function(a, e) {
    return a.concat([ e.slice(1) ]);
  }
  if (args[0].length === 0)
    return [];
  return [ _reduce(accumulateheads, args, []) ]
           .concat(_zip(...(_reduce(accumulatetails, args, []))));
}


const _compose = function(f, g) {
  return function(x) {
    return f(g(x));
  }
}


const _pipe = function(l) {
  const accumulate = function(a, e) {
    return e(a);
  }
  return function(v) {
    return _reduce(accumulate, l, v);
  }
}


const _pipe2 = function(l) {
  return _reduce(_compose, _reverse(l));
}


const _pipemaybe = function(l) {
  const accumulate = function(a, e) {
    if (a !== null)
      return e(a);
    else
      return null;
  }
  return function(v) {
    return _reduce(accumulate, l, v);
  }
}


const _partial = function(f, ...args) {
  let args1 = args;
  return function(...args) {
    return f.apply(null, args1.concat(args));
  }
}


const _curry = function(f, arity) {
  arity = arity || f.length;

  return function(v) {
    if (arity === 1)
      return f(v);
    else
      return _curry(_partial(f, v), arity - 1);
  }
}


const _memoize = function(f) {
  let cache = {};

  return function(...args) {
    let key = JSON.stringify(args);
    if (key in cache)
      return cache[key];
    else
      return cache[key] = f(...args);
  }
}


const factorial = function(n) {
  if (n <= 1)
    return 1;
  else
    return n * factorial(n - 1);
}


const fibonacci = function(n) {
  if (n <= 1)
    return 1;
  else
    return fibonacci(n - 1) + fibonacci(n - 2);
}


const memoizedfibonacci = function(n) {
  const internal = function(f, n) {
    if (n <= 1)
      return 1;
    else
      return f(f, n - 1) + f(f, n - 2);
  }
  let f = _memoize(internal)
  return f(f, n)
}


const primes = function(n) {
  const notdivisibleby = function(y, x) {
    return x % y !== 0;
  }

  const sieve = function(f, l) {
    if (l.length === 0)
      return [];
    else
      return [ l[0] ].concat(sieve(f, _filter(_partial(f, l[0]), l.slice(1))));
  }

  return sieve(notdivisibleby, _range(2, n));
}


const ispalindrome = function(s) {
  if (s.length === 0)
    return true;
  else if (s.slice(0, 1) != s.slice(-1))
    return false;
  else
    return ispalindrome(s.slice(1, -1));
}


module.exports = {
  '_flatten':          _flatten,
  '_range':            _range,
  '_reverse':          _reverse,
  '_reduce':           _reduce,
  '_map':              _map,
  '_filter':           _filter,
  '_partition':        _partition,
  '_sort':             _sort,
  '_unique':           _unique,
  '_zip':              _zip,
  '_compose':          _compose,
  '_pipe':             _pipe,
  '_pipe2':            _pipe2,
  '_pipemaybe':        _pipemaybe,
  '_partial':          _partial,
  '_curry':            _curry,
  '_memoize':          _memoize,
  'factorial':         factorial,
  'fibonacci':         fibonacci,
  'memoizedfibonacci': memoizedfibonacci,
  'primes':            primes,
  'ispalindrome':      ispalindrome
};
