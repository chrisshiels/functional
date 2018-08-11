#!/usr/bin/env node

// 'functional.js'.
// Chris Shiels.


'use strict';


const trampoline = function(f) {
  const internal = function(...args) {
    let v = f(...args);
    while (v instanceof Function)
      v = v();
    return v;
  }
  return internal;
}


const all_recursive = function(f, l) {
  const all = function(f, l) {
    if (l.length === 0)
      return false;
    else if (l.length === 1)
      return f(l[0]);
    else
      return f(l[0]) && all(f, l.slice(1));
  }
  return all(f, l);
}


const all_accumulator = function(f, l) {
  const all = function(f, l, a = true) {
    if (l.length === 0)
      return false;
    else if (l.length === 1)
      return a;
    else
      return () => all(f, l.slice(1), f(l[0]) && a);
  }
  return trampoline(all)(f, l);
}


const all_callbacks = function(f, l) {
  const all = function(f, l, c = (v) => v) {
    if (l.length === 0)
      return c(false);
    else if (l.length === 1)
      return c(f(l[0]));
    else
      return () => all(f, l.slice(1), (v) => () => c(f(l[0]) && v));
  }
  return trampoline(all)(f, l);
}


const all = all_callbacks;


const any_recursive = function(f, l) {
  const any = function(f, l) {
    if (l.length === 0)
      return false;
    else if (l.length === 1)
      return f(l[0]);
    else
      return f(l[0]) || any(f, l.slice(1));
  }
  return any(f, l);
}


const any_accumulator = function(f, l) {
  const any = function(f, l, a = true) {
    if (l.length === 0)
      return false;
    else if (l.length === 1)
      return a;
    else
      return () => any(f, l.slice(1), f(l[0]) || a);
  }
  return trampoline(any)(f, l);
}


const any_callbacks = function(f, l) {
  const any = function(f, l, c = (v) => v) {
    if (l.length === 0)
      return c(false);
    else if (l.length === 1)
      return c(f(l[0]));
    else
      return () => any(f, l.slice(1), (v) => () => c(f(l[0]) || v));
  }
  return trampoline(any)(f, l);
}


const any = any_callbacks;


const flatten_recursive = function(l) {
  const flatten = function(l) {
    if (l.length === 0)
      return [];
    else if (l[0] instanceof Array)
      return flatten(l[0]).concat(flatten(l.slice(1)));
    else
      return [ l[0] ].concat(flatten(l.slice(1)));
  }
  return flatten(l);
}


const flatten_accumulator = function(l) {
  const flatten = function(l, a = []) {
    if (l.length === 0)
      return a;
    else if (l[0] instanceof Array)
      return () => flatten(l[0].concat(l.slice(1)), a);
    else
      return () => flatten(l.slice(1), a.concat([ l[0] ]));
  }
  return trampoline(flatten)(l);
}


const flatten_callbacks = function(l) {
  const flatten = function(l, c = (v) => v) {
    if (l.length === 0)
      return c([]);
    else if (l[0] instanceof Array)
      return () => flatten(l[0].concat(l.slice(1)), (v) => () => c(v));
    else
      return () => flatten(l.slice(1), (v) => () => c([ l[0] ].concat(v)));
  }
  return trampoline(flatten)(l);
}


const flatten = flatten_callbacks;


const range_recursive = function(m, n = null, s = 1) {
  const range = function(m, n = null, s = 1) {
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
  return range(m, n, s);
}


const range_accumulator = function(m, n = null, s = 1) {
  const range = function(m, n = null, s = 1) {
    const internal = function(start, stop, step, a = []) {
      if (step === 0 ||
          (step > 0 && start >= stop) ||
          (step < 0 && start <= stop))
        return a;
      else
        return () => internal(start + step,
                              stop,
                              step,
                              a.concat([ start ]));
    }
    if (n === null)
      return internal(0, m, s);
    else
      return internal(m, n, s);
  }
  return trampoline(range)(m, n, s);
}


const range_callbacks = function(m, n = null, s = 1) {
  const range = function(m, n = null, s = 1) {
    const internal = function(start, stop, step, c = (v) => v) {
      if (step === 0 ||
          (step > 0 && start >= stop) ||
          (step < 0 && start <= stop))
        return c([]);
      else
        return () => internal(start + step,
                              stop,
                              step,
                              (v) => () => c([ start ].concat(v)));
    }
    if (n === null)
      return internal(0, m, s);
    else
      return internal(m, n, s);
  }
  return trampoline(range)(m, n, s);
}


const range = range_callbacks;


const reduce = function(f, l, v = null) {
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


const map = function(f, l) {
  const accumulate = function(a, e) {
    return a.concat([ f(e) ]);
  }
  return reduce(accumulate, l, []);
}


const filter = function(f, l) {
  const accumulate = function(a, e) {
    if (f(e))
      return a.concat([ e ]);
    else
      return a;
  }
  return reduce(accumulate, l, []);
}


const partition = function(f, l) {
  const accumulate = function(a, e) {
    let left, right;
    [ left, right ] = a;
    if (f(e))
      return [ left.concat([ e ]), right ];
    else
      return [ left, right.concat([ e ]) ];
  }
  return reduce(accumulate, l, [ [], [] ]);
}


const split = function(f, l) {
  const accumulate = function(a, e) {
    if (f(e))
      return a.concat([ [] ]);
    else {
      return a.slice(0, -1).concat([ a.slice(-1)[0].concat(e) ]);
    }
  }

  const internal = function(e) {
    return e.length !== 0;
  }

  return filter(internal, reduce(accumulate, l, [ [] ]));
}


const reverse = function(l) {
  const accumulate = function(a, e) {
    return [ e ].concat(a);
  }
  return reduce(accumulate, l, []);
}


const sort = function(f, l) {
  if (l.length === 0)
    return [];
  return sort(f, filter((e) => { return f(e, l[0]); }, l.slice(1)))
           .concat([ l[0] ])
           .concat(sort(f, filter((e) => { return !f(e, l[0]); }, l.slice(1))));
}


const unique = function(l) {
  const accumulate = function(a, e) {
    if (a.includes(e))
      return a;
    else
      return a.concat([ e ]);
  }
  return reduce(accumulate, l, []);
}


const zip = function(...args) {
  const accumulateheads = function(a, e) {
    return a.concat([ e[0] ]);
  }
  const accumulatetails = function(a, e) {
    return a.concat([ e.slice(1) ]);
  }
  if (args[0].length === 0)
    return [];
  return [ reduce(accumulateheads, args, []) ]
           .concat(zip(...(reduce(accumulatetails, args, []))));
}


const permutations = function(l) {
  if (l.length === 0)
    return [];
  else if (l.length === 1)
    return [ l ];
  else
    return reduce((a, e1) =>
	            { return a.concat(map((e2) =>
		                        { return [ e1 ].concat(e2) },
	                                    permutations(filter((e3) =>
						           { return e3 != e1 },
						         l)))) },
		   l,
	           []);
}


const compose = function(f1, f2) {
  return function(v) {
    return f2(f1(v));
  }
}


const pipe = function(l) {
  const accumulate = function(a, e) {
    return e(a);
  }
  return function(v) {
    return reduce(accumulate, l, v);
  }
}


const pipe2 = function(l) {
  return reduce(compose, l);
}


const pipemaybe = function(l) {
  const accumulate = function(a, e) {
    if (a !== null)
      return e(a);
    else
      return null;
  }
  return function(v) {
    return reduce(accumulate, l, v);
  }
}


const partial = function(f, ...args1) {
  return function(...args2) {
    return f(...args1.concat(args2));
  }
}


const curry = function(f, arity) {
  arity = arity || f.length;

  return function(v) {
    if (arity === 1)
      return f(v);
    else
      return curry(partial(f, v), arity - 1);
  }
}


const memoize = function(f) {
  let cache = {};

  return function(...args) {
    let key = JSON.stringify(args);
    if (!(key in cache))
      cache[key] = f(...args);
    return cache[key];
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
  let fibonacci = function(n) {
    if (n <= 1)
      return 1;
    else
      return fibonacci(n - 1) + fibonacci(n - 2);
  }
  fibonacci = memoize(fibonacci);
  return fibonacci(n);
}


const primes = function(n) {
  const sieve = function(l) {
    if (l.length === 0)
      return [];
    else
      return [ l[0] ].concat(sieve(filter((e) => { return e % l[0] != 0 },
                                          l.slice(1))));
  }

  return sieve(range(2, n));
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
  'all_recursive':       all_recursive,
  'all_accumulator':     all_accumulator,
  'all_callbacks':       all_callbacks,
  'all':                 all,
  'any_recursive':       any_recursive,
  'any_accumulator':     any_accumulator,
  'any_callbacks':       any_callbacks,
  'any':                 any,
  'flatten_recursive':   flatten_recursive,
  'flatten_accumulator': flatten_accumulator,
  'flatten_callbacks':   flatten_callbacks,
  'flatten':             flatten,
  'range_recursive':     range_recursive,
  'range_accumulator':   range_accumulator,
  'range_callbacks':     range_callbacks,
  'range':               range,
  'reduce':              reduce,
  'map':                 map,
  'filter':              filter,
  'partition':           partition,
  'split':               split,
  'reverse':             reverse,
  'sort':                sort,
  'unique':              unique,
  'zip':                 zip,
  'permutations':        permutations,
  'compose':             compose,
  'pipe':                pipe,
  'pipe2':               pipe2,
  'pipemaybe':           pipemaybe,
  'partial':             partial,
  'curry':               curry,
  'memoize':             memoize,
  'factorial':           factorial,
  'fibonacci':           fibonacci,
  'memoizedfibonacci':   memoizedfibonacci,
  'primes':              primes,
  'ispalindrome':        ispalindrome
};
