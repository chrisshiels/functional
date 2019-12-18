#!/usr/bin/env node

// 'functional.js'.
// Chris Shiels.


'use strict';


const all = function(f, l) {
  if (l.length === 0)
    return false;
  else if (l.length === 1)
    return f(l[0]);
  else
    return f(l[0]) && all(f, l.slice(1));
}


const any = function(f, l) {
  if (l.length === 0)
    return false;
  else if (l.length === 1)
    return f(l[0]);
  else
    return f(l[0]) || any(f, l.slice(1));
}


const flatten = function(l) {
  if (l.length === 0)
    return [];
  else if (l[0] instanceof Array)
    return flatten(l[0]).concat(flatten(l.slice(1)));
  else
    return [ l[0] ].concat(flatten(l.slice(1)));
}


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


const scan = function(f, l, v) {
  const internal = function(f, l, a) {
    if (l.length === 0)
      return a;
    else
      return internal(f, l.slice(1), a.concat(f(a.slice(-1)[0], l[0])));
  }
  return internal(f, l, [ v ]);
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


const zip = function(l1, l2) {
  if (l1.length === 0 || l2.length === 0)
    return [];
  else
    return [ (l1[0], l2[0]) ].concat(zip(l1.slice(1), l2.slice(1)));
}


const zipwith = function(f, l1, l2) {
  if (l1.length === 0 || l2.length === 0)
    return [];
  else
    return [ f(l1[0], l2[0]) ].concat(zipwith(f, l1.slice(1), l2.slice(1)));
}


const group = function(l) {
  const accumulate = function(a, e) {
    if (a.length && a.slice(-1)[0].includes(e))
      return a.slice(0, -1).concat([ a.slice(-1)[0].concat([ e ]) ]);
    else
      return a.concat([ [ e ] ]);
  }
  return reduce(accumulate, l, []);
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


const flip = function(f) {
  return function(...args) {
    return f(...reverse(args));
  }
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
      return a;
  }
  return function(v) {
    return reduce(accumulate, l, v);
  }
}


const pipeeither = function(l) {
  const accumulate = function(a, e) {
    if (a[0] === null)
      return e(a[1]);
    else
      return a;
  }
  return function(v) {
    return reduce(accumulate, l, [null, v]);
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
  if (n === 1 || n === 2)
    return 1;
  else
    return fibonacci(n - 1) + fibonacci(n - 2);
}


const memoizedfibonacci = function(n) {
  let fibonacci = function(n) {
    if (n === 1 || n === 2)
      return 1;
    else
      return fibonacci(n - 1) + fibonacci(n - 2);
  }
  fibonacci = memoize(fibonacci);
  return fibonacci(n);
}


const tablefibonacci = function(n) {
  const fibonacci = function(a, e) {
    if (e === 1 || e === 2)
      return a.concat([ 1 ]);
    else
      return a.concat([ a.slice(-1)[0] + a.slice(-2)[0] ]);
  }
  return reduce(fibonacci, range(1, n + 1), []).slice(-1);
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
  'all':               all,
  'any':               any,
  'flatten':           flatten,
  'range':             range,
  'reduce':            reduce,
  'scan':              scan,
  'map':               map,
  'filter':            filter,
  'partition':         partition,
  'split':             split,
  'reverse':           reverse,
  'sort':              sort,
  'unique':            unique,
  'zip':               zip,
  'zipwith':           zipwith,
  'group':             group,
  'permutations':      permutations,
  'flip':              flip,
  'compose':           compose,
  'pipe':              pipe,
  'pipe2':             pipe2,
  'pipemaybe':         pipemaybe,
  'pipeeither':        pipeeither,
  'partial':           partial,
  'curry':             curry,
  'memoize':           memoize,
  'factorial':         factorial,
  'fibonacci':         fibonacci,
  'memoizedfibonacci': memoizedfibonacci,
  'tablefibonacci':    tablefibonacci,
  'primes':            primes,
  'ispalindrome':      ispalindrome
};
