#!/usr/bin/env node

// 'test.js'.
// Chris Shiels.


'use strict';


const assert = require('assert');
const functional = require('./functional');


describe('functional', function() {
  describe('#_range()', function() {
    it('returns [ 0..9 ] for _range(10)',
       function() {
         assert.deepEqual(functional._range(10),
                          [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]);
    });

    it('returns [ 1..10 ] for _range(11, 1)',
       function() {
         assert.deepEqual(functional._range(11, 1),
                          [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]);
    });
  });


  describe('#_reduce()', function() {
    it('returns 55 for _reduce((a, e) => { return a + e; }, _range(11, 1), 0)',
       function() {
         assert.equal(functional._reduce((a, e) => { return a + e; },
                                         functional._range(11, 1),
                                         0),
                      55);
    });
    it('returns 55 for _reduce((a, e) => { return a + e; }, _range(11, 1))',
       function() {
         assert.equal(functional._reduce((a, e) => { return a + e; },
                                         functional._range(11, 1)),
                      55);
    });
  });


  describe('#_map()', function() {
    it('returns [ 2,4,6..20 ] for _map((e) => { return e * 2; }, _range(11, 1))',
       function() {
         assert.deepEqual(functional._map((e) => { return e * 2; },
                                          functional._range(11, 1)),
                          [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 ]);
    });
  });


  describe('#_filter()', function() {
    it('returns [ 2,4,6,8,10 ] for _filter((e) => { return e % 2 === 0; }, _range(11, 1))',
       function() {
         assert.deepEqual(functional._filter((e) => { return e % 2 === 0; },
                                             functional._range(11, 1)),
                          [ 2, 4, 6, 8, 10 ]);
    });

    it('returns [ 1,3,5,7,9 ] for _filter((e) => { return e % 2 === 1; }, _range(11, 1))',
       function() {
         assert.deepEqual(functional._filter((e) => { return e % 2 === 1; },
                                             functional._range(11, 1)),
                          [ 1, 3, 5, 7, 9 ]);
    });
  });


  describe('#_partition()', function() {
    it('returns [ [ 3, 6, 9 ], [ 1, 2, 4, 5, 7, 8, 10 ] ] for _partition((e) => { return e % 3 === 0; }, _range(11, 1))',
       function() {
         assert.deepEqual(functional._partition((e) => { return e % 3 === 0; },
                                                functional._range(11, 1)),
                          [ [ 3, 6, 9 ], [ 1, 2, 4, 5, 7, 8, 10 ] ]);
    });

    it('returns [ [ 1, 2, 4, 5, 7, 8, 10 ], [ 3, 6, 9 ] ] for _partition((e) => { return e % 3 !== 0; }, _range(11, 1))',
       function() {
         assert.deepEqual(functional._partition((e) => { return e % 3 !== 0; },
                                                functional._range(11, 1)),
                          [ [ 1, 2, 4, 5, 7, 8, 10 ], [ 3, 6, 9 ] ]);
    });

    it('returns [ [], [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] ] for _partition((e) => { return e === 0; }, _range(11, 1))',
       function() {
         assert.deepEqual(functional._partition((e) => { return e === 0; },
                                                functional._range(11, 1)),
                          [ [], [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] ]);
    });
  });


  describe('#_reverse()',function() {
    it('returns [ 10..1 ] for _reverse(_range(11, 1))',
       function() {
         assert.deepEqual(functional._reverse(functional._range(11, 1)),
                          [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]);
    });
  });


  describe('#_sort()', function() {
    it('returns [ 1..10 ] for _sort((m, n) => { return m <= n; }, [ 1, 10, 2, 9, 3, 8, 4, 7, 5, 6 ])',
       function() {
         assert.deepEqual(functional._sort((m, n) => { return m <= n; },
                                           [ 1, 10, 2, 9, 3, 8, 4, 7, 5, 6 ]),
                          [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]);
    });
  });


  describe('#_unique()', function() {
    it('returns [ 5,1,4,2,3 ] for _unique([ 5, 1, 4, 2, 3, 3, 2, 4, 1, 5 ])',
       function() {
         assert.deepEqual(functional._unique([ 5, 1, 4, 2, 3, 3, 2, 4, 1, 5 ]),
                          [ 5, 1, 4, 2, 3 ]);
    });
  });


  describe('#_zip()', function() {
    it('returns [ [ 1, 5 ], [ 2, 6 ], [ 3, 7 ], [ 4, 8 ] ] for _zip(...[ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ] ])',
       function() {
         let a = [ [ 1, 2, 3, 4 ],
                   [ 5, 6, 7, 8 ] ];
         let a1 = [ [ 1, 5 ],
                    [ 2, 6 ],
                    [ 3, 7 ],
                    [ 4, 8 ] ];
         assert.deepEqual(functional._zip(...a),
                          a1);
    });

    it('returns [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ] ] for _zip(..._zip(...[ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ] ]))',
       function() {
         let a = [ [ 1, 2, 3, 4 ],
                   [ 5, 6, 7, 8 ] ];
         assert.deepEqual(functional._zip(...functional._zip(...a)),
                          a);
    });
  });


  describe('#_compose()', function() {
    it('returns 3 for _compose(valueadd1, valuemultiply2)(1)',
       function() {
         const valueadd1 = function(v) {
           return v + 1;
         }

         const valuemultiply2 = function(v) {
           return v * 2;
         }

         assert.equal(functional._compose(valueadd1, valuemultiply2)(1),
                      3);
    });
  });


  describe('#_pipe()', function() {
    it('returns 5 for _pipe([ valueadd1, valuemultiply2, valueadd1 ])(1)',
       function() {
         const valueadd1 = function(v) {
           return v + 1;
         }

         const valuemultiply2 = function(v) {
           return v * 2;
         }

         assert.equal(functional._pipe([ valueadd1,
                                         valuemultiply2,
                                         valueadd1 ])(1),
                      5);
    });

    it('returns [ 5,7,9,11,13,15,17,19,21,23 ] for _pipe([ listadd1, listmultiply2, listadd1 ])(_range(11, 1))',
       function() {
         const listadd1 = function(l) {
           return functional._map((e) => { return e + 1; }, l);
         }

         const listmultiply2 = function(l) {
           return functional._map((e) => { return e * 2; }, l);
         }

         assert.deepEqual(functional._pipe([ listadd1,
                                             listmultiply2,
                                             listadd1 ])(functional._range(11, 1)),
                          [ 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 ]);
    });
  });


  describe('#_pipe2()', function() {
    it('returns 5 for _pipe2([ valueadd1, valuemultiply2, valueadd1 ])(1)',
       function() {
         const valueadd1 = function(v) {
           return v + 1;
         }

         const valuemultiply2 = function(v) {
           return v * 2;
         }

         assert.equal(functional._pipe2([ valueadd1,
                                         valuemultiply2,
                                         valueadd1 ])(1),
                      5);
    });

    it('returns [ 5,7,9,11,13,15,17,19,21,23 ] for _pipe2([ listadd1, listmultiply2, listadd1 ])(_range(11, 1))',
       function() {
         const listadd1 = function(l) {
           return functional._map((e) => { return e + 1; }, l);
         }

         const listmultiply2 = function(l) {
           return functional._map((e) => { return e * 2; }, l);
         }

         assert.deepEqual(functional._pipe2([ listadd1,
                                             listmultiply2,
                                             listadd1 ])(functional._range(11, 1)),
                          [ 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 ]);
    });
  });


  describe('#_partial()', function() {
    it('returns [ 11..20 ] for _map(_partial(add, 10), _range(11, 1))',
       function() {
         const add = function(a, b) {
           return a + b;
         }

         const add10 = function(x) {
           return add(x, 10);
         }

         assert.deepEqual(functional._map(add10,
                                          functional._range(11, 1)),
                          [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]);

         assert.deepEqual(functional._map(functional._partial(add, 10),
                                          functional._range(11, 1)),
                          [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]);
    });
  });


  describe('#_curry()', function() {
    it('supports multiple execution paths',
       function() {
         const args = function(...a) {
           return a;
         }

         let cargs = functional._curry(args, 5)
         let cargsab = cargs('a')('b')

         assert.deepEqual(cargsab('c')('d')('e'),
                          [ 'a', 'b', 'c', 'd', 'e' ]);
         assert.deepEqual(cargsab('x')('y')('z'),
                          [ 'a', 'b', 'x', 'y', 'z' ]);
         assert.deepEqual(cargsab('c')('d')('e'),
                          [ 'a', 'b', 'c', 'd', 'e' ]);
         assert.deepEqual(cargsab('x')('y')('z'),
                          [ 'a', 'b', 'x', 'y', 'z' ]);
    });

    it('returns 15 for _curry(add, 2)(10)(5) and 25 for _curry(add, 2)(20)(5)',
       function() {
         const add = function(a, b) {
           return a + b;
         }

         let cadd = functional._curry(add, 2)

         assert.equal(cadd(10)(5),
                      15);
         assert.equal(cadd(20)(5),
                      25);
    });

    it('returns [ 11..20 ] for _map(_curry(add, 2)(10), _range(11, 1))',
       function() {
         const add = function(a, b) {
           return a + b;
         }

         assert.deepEqual(functional._map(functional._curry(add, 2)(10),
                                          functional._range(11, 1)),
                          [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]);
    });
  });


  describe('#factorial()', function() {
    it('returns [ 1,2,6,24,120,720,5040,40320,362880,3628800 ] for _map(factorial, _range(11, 1))',
       function() {
         assert.deepEqual(functional._map(functional.factorial,
                                          functional._range(11, 1)),
                          [ 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800 ]);
    });
  });


  describe('#fibonacci()', function() {
    it('returns [ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ] for _map(fibonacci, _range(11, 1))',
       function() {
         assert.deepEqual(functional._map(functional.fibonacci,
                                          functional._range(11, 1)),
                          [ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ]);
    });
  });


  describe('#memoizedfibonacci()', function() {
    it('returns 20365011074 for memoizedfibonacci(50)',
       function() {
         assert.equal(functional.memoizedfibonacci(50),
                      20365011074);
    });
  });


  describe('#primes()', function() {
    it('returns [ 2, 3, 5, 7, 11, 13, 17, 19 ] for primes(20)',
       function() {
         assert.deepEqual(functional.primes(20),
                          [ 2, 3, 5, 7, 11, 13, 17, 19 ]);
    });
  });


  describe('#ispalindrome()', function() {
    it('returns true for ispalindrome(\'tattarrattat\')',
       function() {
         assert.equal(functional.ispalindrome('tattarrattat'),
                      true);
    });
  });
});
