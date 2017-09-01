# functional/javascript

Implementations of common functional programming functions in JavaScript:
range, reduce, map, filter, reverse, sort, unique, zip, compose, pipe,
partial, curry and memoize.

    host$ npm install
    host$ npm test
    
    > functional@1.0.0 test /home/chris/gu/github.com/functional/javascript
    > mocha
    
    
    
      functional
        #_range()
          ✓ returns [ 0..9 ] for _range(10)
          ✓ returns [ 1..10 ] for _range(11, 1)
        #_reverse()
          ✓ returns [ 10..1 ] for _reverse(_range(11, 1))
        #_reduce()
          ✓ returns 55 for _reduce((a, e) => { return a + e; }, _range(11, 1), 0)
        #_map()
          ✓ returns [ 2,4,6..20 ] for _map((e) => { return e * 2; }, _range(11, 1))
        #_filter()
          ✓ returns [ 2,4,6,8,10 ] for _filter((e) => { return e % 2 === 0; }, _range(11, 1))
          ✓ returns [ 1,3,5,7,9 ] for _filter((e) => { return e % 2 === 1; }, _range(11, 1))
        #_sort()
          ✓ returns [ 1..10 ] for _sort((m, n) => { return m <= n; }, [ 1, 10, 2, 9, 3, 8, 4, 7, 5, 6 ])
        #_unique()
          ✓ returns [ 5,1,4,2,3 ] for _unique([ 5, 1, 4, 2, 3, 3, 2, 4, 1, 5 ])
        #_zip()
          ✓ returns [ [ 1, 5 ], [ 2, 6 ], [ 3, 7 ], [ 4, 8 ] ] for _zip(...[ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ] ])
          ✓ returns [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ] ] for _zip(..._zip(...[ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ] ]))
        #_compose()
          ✓ returns 3 for _compose(valueadd1, valuemultiply2)(1)
        #_pipe()
          ✓ returns 5 for _pipe([ valueadd1, valuemultiply2, valueadd1 ])(1)
          ✓ returns [ 5,7,9,11,13,15,17,19,21,23 ] for _pipe([ listadd1, listmultiply2, listadd1 ])(_range(11, 1))
        #_partial()
          ✓ returns [ 11..20 ] for _map(_partial(add, 10), _range(11, 1))
        #_curry()
          ✓ supports multiple execution paths
          ✓ returns 15 for _curry(add, 2)(10)(5) and 25 for _curry(add, 2)(20)(5)
          ✓ returns [ 11..20 ] for _map(_curry(add, 2)(10), _range(11, 1))
        #factorial()
          ✓ returns [ 1,2,6,24,120,720,5040,40320,362880,3628800 ] for _map(factorial, _range(11, 1))
        #fibonacci()
          ✓ returns [ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ] for _map(fibonacci, _range(11, 1))
        #memoizedfibonacci()
          ✓ returns 20365011074 for memoizedfibonacci(50)
        #primes()
          ✓ returns [ 2, 3, 5, 7, 11, 13, 17, 19 ] for primes(20)
        #ispalindrome()
          ✓ returns true for ispalindrome('tattarrattat')
    
    
      23 passing (33ms)
