#!/usr/bin/env node

// 'test.js'.
// Chris Shiels.


'use strict';


const assert = require('assert');
const functional = require('./functional');


describe('functional', function() {
  describe('#all()', function() {
    const divisibleby2 = function(v) {
      return v % 2 === 0;
    }

    const divisibleby3 = function(v) {
      return v % 3 === 0;
    }

    it('returns false for all(divisibleby2, [])',
       function() {
         assert.equal(functional.all(divisibleby2, []),
                      false);
    });

    it('returns true for all(divisibleby2, [ 2, 4, 6, 8, 10 ])',
       function() {
         assert.equal(functional.all(divisibleby2, [ 2, 4, 6, 8, 10 ]),
                      true);
    });

    it('returns false for all(divisibleby3, [ 2, 4, 6, 8, 10 ])',
       function() {
         assert.equal(functional.all(divisibleby3, [ 2, 4, 6, 8, 10 ]),
                      false);
    });
  });


  describe('#any()', function() {
    const divisibleby2 = function(v) {
      return v % 2 === 0;
    }

    const divisibleby3 = function(v) {
      return v % 3 === 0;
    }

    it('returns false for any(divisibleby2, [])',
       function() {
         assert.equal(functional.any(divisibleby2, []),
                      false);
    });

    it('returns true for any(divisibleby2, [ 2, 4, 6, 8, 10 ])',
       function() {
         assert.equal(functional.any(divisibleby2, [ 2, 4, 6, 8, 10 ]),
                      true);
    });

    it('returns true for any(divisibleby3, [ 2, 4, 6, 8, 10 ])',
       function() {
         assert.equal(functional.any(divisibleby3, [ 2, 4, 6, 8, 10 ]),
                      true);
    });
  });


  describe('#flatten()', function() {
    it('returns [] for flatten([])',
       function() {
         assert.deepEqual(functional.flatten([]),
                          []);
    });

    it('returns [ 1, 2, 3 ] for flatten([ 1, 2, 3 ])',
       function() {
         assert.deepEqual(functional.flatten([ 1, 2, 3 ]),
                          [ 1, 2, 3 ]);
    });

    it('returns [ 1, 2, 3 ] for flatten([[ 1, 2 ], 3])',
       function() {
         assert.deepEqual(functional.flatten([[ 1, 2 ], 3]),
                          [ 1, 2, 3 ]);
    });

    it('returns [ 1, 2, 3 ] for flatten([1, [ 2, 3 ]])',
       function() {
         assert.deepEqual(functional.flatten([1, [ 2, 3 ]]),
                          [ 1, 2, 3 ]);
    });

    it('returns [ 1, 2, 3 ] for flatten([1, [ 2, [ 3 ] ] ])',
       function() {
         assert.deepEqual(functional.flatten([1, [ 2, [ 3 ] ] ]),
                          [ 1, 2, 3 ]);
    });

    it('returns [ 1, 2, 3 ] for flatten([ [ [ 1 ], [ 2 ], [ 3 ] ] ])',
       function() {
         assert.deepEqual(functional.flatten([ [ [ 1 ], [ 2 ], [ 3 ] ] ]),
                          [ 1, 2, 3 ]);
    });
  });


  describe('#range()', function() {
    it('returns [] for range(0)',
       function() {
         assert.deepEqual(functional.range(0),
                          []);
    });

    it('returns [ 0..9 ] for range(10)',
       function() {
         assert.deepEqual(functional.range(10),
                          [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]);
    });

    it('returns [ 0..9 ] for range(0, 10)',
       function() {
         assert.deepEqual(functional.range(0, 10),
                          [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]);
    });

    it('returns [ 0..9 ] for range(0, 10, 1)',
       function() {
         assert.deepEqual(functional.range(0, 10, 1),
                          [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]);
    });

    it('returns [ 0,2,4,6,8 ] for range(0, 10, 2)',
       function() {
         assert.deepEqual(functional.range(0, 10, 2),
                          [ 0, 2, 4, 6, 8 ]);
    });

    it('returns [ 0,3,6,9 ] for range(0, 10, 3)',
       function() {
         assert.deepEqual(functional.range(0, 10, 3),
                          [ 0, 3, 6, 9 ]);
    });

    it('returns [ 10..1 ] for range(10, 0, -1)',
       function() {
         assert.deepEqual(functional.range(10, 0, -1),
                          [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]);
    });

    it('returns [ 1..10 ] for range(1, 11)',
       function() {
         assert.deepEqual(functional.range(1, 11),
                          [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]);
    });
  });


  describe('#reduce()', function() {
    it('returns 55 for reduce((a, e) => { return a + e; }, range(1, 11), 0)',
       function() {
         assert.equal(functional.reduce((a, e) => { return a + e; },
                                        functional.range(1, 11),
                                        0),
                      55);
    });

    it('returns 55 for reduce((a, e) => { return a + e; }, range(1, 11))',
       function() {
         assert.equal(functional.reduce((a, e) => { return a + e; },
                                        functional.range(1, 11)),
                      55);
    });

    it('returns [ 1, 2, 3, 4, 5, 6 ] for reduce((a, e) => { return a.concat(e); }, [ [ 1 ], [ 2, 3 ], [ 4, 5, 6 ] ])',
       function() {
         assert.deepEqual(functional.reduce((a, e) => { return a.concat(e); },
                                            [ [ 1 ], [ 2, 3 ], [ 4, 5, 6 ] ]),
                          [ 1, 2, 3, 4, 5, 6 ]);
    });

    it('returns 6 for reduce((a, e) => { return a + e.length; }, [ [ 1 ], [ 2, 3 ], [ 4, 5, 6 ] ], 0)',
       function() {
         assert.equal(functional.reduce((a, e) => { return a + e.length; },
                                        [ [ 1 ], [ 2, 3 ], [ 4, 5, 6 ] ],
	                                0),
                      6);
    });
  });


  describe('#scan()', function() {
    it('returns [ 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55 ] for scan((a, e) => { return a + e; }, range(1, 11), 0)',
       function() {
         assert.deepEqual(functional.scan((a, e) => { return a + e; },
                                          functional.range(1, 11),
                                          0),
                          [ 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55 ]);
    });
  });


  describe('#map()', function() {
    it('returns [ 2,4,6..20 ] for map((e) => { return e * 2; }, range(1, 11))',
       function() {
         assert.deepEqual(functional.map((e) => { return e * 2; },
                                         functional.range(1, 11)),
                          [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 ]);
    });

    it('returns [ [ 1 ], [ 2 ], [ 3 ] ] for map((e) => { return e; }, [ [ 1 ], [ 2 ], [ 3 ] ])',
       function() {
         assert.deepEqual(functional.map((e) => { return e; },
                                         [ [ 1 ], [ 2 ], [ 3 ] ]),
                          [ [ 1 ], [ 2 ], [ 3 ] ]);
    });
  });


  describe('#filter()', function() {
    it('returns [ 2, 4, 6, 8, 10 ] for filter((e) => { return e % 2 === 0; }, range(1, 11))',
       function() {
         assert.deepEqual(functional.filter((e) => { return e % 2 === 0; },
                                            functional.range(1, 11)),
                          [ 2, 4, 6, 8, 10 ]);
    });

    it('returns [ 1, 3, 5, 7, 9 ] for filter((e) => { return e % 2 === 1; }, range(1, 11))',
       function() {
         assert.deepEqual(functional.filter((e) => { return e % 2 === 1; },
                                            functional.range(1, 11)),
                          [ 1, 3, 5, 7, 9 ]);
    });

    it('returns [ [ 1 ], [ 2 ], [ 3 ] ] for filter((e) => { return e.length !== 0; }, [ [ 1 ], [], [ 2 ], [], [ 3 ] ])',
       function() {
         assert.deepEqual(functional.filter((e) => { return e.length !== 0; },
                                            [ [ 1 ], [], [ 2 ], [], [ 3 ] ]),
                          [ [ 1 ], [ 2 ], [ 3 ] ]);
    });
  });


  describe('#partition()', function() {
    it('returns [ [ 3, 6, 9 ], [ 1, 2, 4, 5, 7, 8, 10 ] ] for partition((e) => { return e % 3 === 0; }, range(1, 11))',
       function() {
         assert.deepEqual(functional.partition((e) => { return e % 3 === 0; },
                                               functional.range(1, 11)),
                          [ [ 3, 6, 9 ], [ 1, 2, 4, 5, 7, 8, 10 ] ]);
    });

    it('returns [ [ 1, 2, 4, 5, 7, 8, 10 ], [ 3, 6, 9 ] ] for partition((e) => { return e % 3 !== 0; }, range(1, 11))',
       function() {
         assert.deepEqual(functional.partition((e) => { return e % 3 !== 0; },
                                               functional.range(1, 11)),
                          [ [ 1, 2, 4, 5, 7, 8, 10 ], [ 3, 6, 9 ] ]);
    });

    it('returns [ [], [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] ] for partition((e) => { return e === 0; }, range(1, 11))',
       function() {
         assert.deepEqual(functional.partition((e) => { return e === 0; },
                                               functional.range(1, 11)),
                          [ [], [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] ]);
    });

    it('returns [ [ [ 1, 2 ], [ 1, 2, 3 ] ], [ [ 1 ] ] ] for partition((e) => { return e.length > 1; }, [ [ 1 ], [ 1, 2 ], [ 1, 2, 3 ] ])',
       function() {
         assert.deepEqual(functional.partition((e) => { return e.length > 1; },
                                               [ [ 1 ], [ 1, 2 ], [ 1, 2, 3 ] ]),
                          [ [ [ 1, 2 ], [ 1, 2, 3 ] ], [ [ 1 ] ] ]);
    });
  });


  describe('#split()', function() {
    it('returns [] for split((e) => { return e % 10 === 0; }, [])',
       function() {
         assert.deepEqual(functional.split((e) => { return e % 10 === 0; },
                                           []),
                          []);
    });

    it('returns [] for split((e) => { return e % 1 === 0; }, range(1, 11))',
       function() {
         assert.deepEqual(functional.split((e) => { return e % 1 === 0; },
                                           functional.range(1, 11)),
                          []);
    });

    it('returns [ [ 1 ], [ 3 ], [ 5 ], [ 7 ], [ 9 ] ] for split((e) => { return e % 2 === 0; }, range(1, 11))',
       function() {
         assert.deepEqual(functional.split((e) => { return e % 2 === 0; },
                                           functional.range(1, 11)),
                          [ [ 1 ], [ 3 ], [ 5 ], [ 7 ], [ 9 ] ]);
    });

    it('returns [ [ 1, 2 ], [ 4, 5 ], [ 7, 8 ], [ 10 ] ] for split((e) => { return e % 3 === 0; }, range(1, 11))',
       function() {
         assert.deepEqual(functional.split((e) => { return e % 3 === 0; },
                                           functional.range(1, 11)),
                          [ [ 1, 2 ], [ 4, 5 ], [ 7, 8 ], [ 10 ] ]);
    });
  });


  describe('#reverse()',function() {
    it('returns [ 10..1 ] for reverse(range(1, 11))',
       function() {
         assert.deepEqual(functional.reverse(functional.range(1, 11)),
                          [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]);
    });

    it('returns [ [ 5, 6 ], [ 3, 4 ], [ 1, 2 ] ] for reverse([ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ] ])',
       function() {
         assert.deepEqual(functional.reverse([ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ] ]),
                          [ [ 5, 6 ], [ 3, 4 ], [ 1, 2 ] ]);
    });
  });


  describe('#sort()', function() {
    it('returns [ 1..10 ] for sort((m, n) => { return m <= n; }, [ 1, 10, 2, 9, 3, 8, 4, 7, 5, 6 ])',
       function() {
         assert.deepEqual(functional.sort((m, n) => { return m <= n; },
                                          [ 1, 10, 2, 9, 3, 8, 4, 7, 5, 6 ]),
                          [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]);
    });

    it('returns [ [ 1 ], [ 1, 2 ],  [ 1, 2, 3 ] ] for sort((m, n) => { return m.length <= n.length; }, [ [ 1, 2, 3], [ 1, 2 ], [ 1 ] ])',
       function() {
         assert.deepEqual(functional.sort((m, n) => { return m.length <= n.length; },
                                          [ [ 1, 2, 3], [ 1, 2 ], [ 1 ] ]),
                          [ [ 1 ], [ 1, 2 ],  [ 1, 2, 3 ] ]);
    });
  });


  describe('#unique()', function() {
    it('returns [ 5, 1, 4, 2, 3 ] for unique([ 5, 1, 4, 2, 3, 3, 2, 4, 1, 5 ])',
       function() {
         assert.deepEqual(functional.unique([ 5, 1, 4, 2, 3, 3, 2, 4, 1, 5 ]),
                          [ 5, 1, 4, 2, 3 ]);
    });
  });


  describe('#zip()', function() {
    it('returns [ (1, 5), (2, 6), (3, 7), (4, 8) ] for zip([ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ])',
       function() {
         let l1 = [ 1, 2, 3, 4 ];
         let l2 = [ 5, 6, 7, 8 ];
         let ret = [ (1, 5),
                     (2, 6),
                     (3, 7),
                     (4, 8) ];
         assert.deepEqual(functional.zip(l1, l2),
                          ret);
    });
  });


  describe('#zipwith()', function() {
    it('returns [ 6, 8, 10, 12 ] for zipwith([ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ])',
       function() {
         let l1 = [ 1, 2, 3, 4 ];
         let l2 = [ 5, 6, 7, 8 ];
         let ret = [ 6,
                     8,
                     10,
                     12 ];
         assert.deepEqual(functional.zipwith((m, n) => { return m + n; },
		                             l1, l2),
                          ret);
    });
  });


  describe('#group()', function() {
    it('returns [ [ 1, 1 ], [ 2 ], [ 3, 3 ], [ 1 ], [ 4, 4, 4 ] ] for group([ 1, 1, 2, 3, 3, 1, 4, 4, 4 ])',
       function() {
         assert.deepEqual(functional.group([ 1, 1, 2, 3, 3, 1, 4, 4, 4 ]),
		          [ [ 1, 1 ], [ 2 ], [ 3, 3 ], [ 1 ], [ 4, 4, 4 ] ]);
    });

    it('returns [ 1, 1, 2, 3, 3, 1, 4, 4, 4 ] for flatten(group([ 1, 1, 2, 3, 3, 1, 4, 4, 4 ]))',
       function() {
         assert.deepEqual(functional.flatten(functional.group([ 1, 1, 2, 3, 3, 1, 4, 4, 4 ])),
		          [ 1, 1, 2, 3, 3, 1, 4, 4, 4 ]);
    });
  });


  describe('#permutations()', function() {
    it('returns [] for permutations([])',
       function() {
         assert.deepEqual(functional.permutations([]),
                          []);
    });

    it('returns [ [ 1 ] ] for permutations([ 1 ])',
       function() {
         assert.deepEqual(functional.permutations([ 1 ]),
                          [ [ 1 ] ]);
    });

    it('returns [ [ 1, 2 ], [ 2, 1 ] ] for permutations([ 1, 2 ])',
       function() {
         assert.deepEqual(functional.permutations([ 1, 2 ]),
                          [ [ 1, 2 ], [ 2, 1 ] ]);
    });

    it('returns [ [ 1, 2, 3 ] .. [ 3, 2, 1 ] ] for permutations([ 1, 2, 3 ])',
       function() {
         assert.deepEqual(functional.permutations([ 1, 2, 3 ]),
                          [ [ 1, 2, 3 ],
                            [ 1, 3, 2 ],
                            [ 2, 1, 3 ],
                            [ 2, 3, 1 ],
                            [ 3, 1, 2 ],
                            [ 3, 2, 1 ] ]);
    });

    it('returns [ [ 1, 2, 3, 4 ] .. [ 4, 3, 2, 1 ] ] for permutations([ 1, 2, 3, 4 ])',
       function() {
         assert.deepEqual(functional.permutations([ 1, 2, 3, 4 ]),
                          [ [ 1, 2, 3, 4 ],
                            [ 1, 2, 4, 3 ],
                            [ 1, 3, 2, 4 ],
                            [ 1, 3, 4, 2 ],
                            [ 1, 4, 2, 3 ],
                            [ 1, 4, 3, 2 ],
                            [ 2, 1, 3, 4 ],
                            [ 2, 1, 4, 3 ],
                            [ 2, 3, 1, 4 ],
                            [ 2, 3, 4, 1 ],
                            [ 2, 4, 1, 3 ],
                            [ 2, 4, 3, 1 ],
                            [ 3, 1, 2, 4 ],
                            [ 3, 1, 4, 2 ],
                            [ 3, 2, 1, 4 ],
                            [ 3, 2, 4, 1 ],
                            [ 3, 4, 1, 2 ],
                            [ 3, 4, 2, 1 ],
                            [ 4, 1, 2, 3 ],
                            [ 4, 1, 3, 2 ],
                            [ 4, 2, 1, 3 ],
                            [ 4, 2, 3, 1 ],
                            [ 4, 3, 1, 2 ],
                            [ 4, 3, 2, 1 ] ]);
    });
  });


  describe('#flip()', function() {
    const subtract = function(x, y) {
      return x - y;
    }

    it('returns 2 for subtract(4, 2)',
       function() {
         assert.equal(subtract(4, 2),
                      2);
    });

    it('returns -2 for flip(subtract)(4, 2)',
       function() {
         assert.equal(functional.flip(subtract)(4, 2),
                      -2);
    });
  });

  describe('#compose()', function() {
    it('returns 3 for compose(valueadd1, valuemultiply2)(1)',
       function() {
         const valueadd1 = function(v) {
           return v + 1;
         }

         const valuemultiply2 = function(v) {
           return v * 2;
         }

         assert.equal(functional.compose(valueadd1, valuemultiply2)(1),
                      4);
    });
  });


  describe('#pipe()', function() {
    it('returns 5 for pipe([ valueadd1, valuemultiply2, valueadd1 ])(1)',
       function() {
         const valueadd1 = function(v) {
           return v + 1;
         }

         const valuemultiply2 = function(v) {
           return v * 2;
         }

         assert.equal(functional.pipe([ valueadd1,
                                        valuemultiply2,
                                        valueadd1 ])(1),
                      5);
    });

    it('returns [ 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 ] for pipe([ listadd1, listmultiply2, listadd1 ])(range(1, 11))',
       function() {
         const listadd1 = function(l) {
           return functional.map((e) => { return e + 1; }, l);
         }

         const listmultiply2 = function(l) {
           return functional.map((e) => { return e * 2; }, l);
         }

         assert.deepEqual(functional.pipe([ listadd1,
                                            listmultiply2,
                                            listadd1 ])(functional.range(1, 11)),
                          [ 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 ]);
    });
  });


  describe('#pipe2()', function() {
    it('returns 5 for pipe2([ valueadd1, valuemultiply2, valueadd1 ])(1)',
       function() {
         const valueadd1 = function(v) {
           return v + 1;
         }

         const valuemultiply2 = function(v) {
           return v * 2;
         }

         assert.equal(functional.pipe2([ valueadd1,
                                         valuemultiply2,
                                         valueadd1 ])(1),
                      5);
    });

    it('returns [ 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 ] for pipe2([ listadd1, listmultiply2, listadd1 ])(range(1, 11))',
       function() {
         const listadd1 = function(l) {
           return functional.map((e) => { return e + 1; }, l);
         }

         const listmultiply2 = function(l) {
           return functional.map((e) => { return e * 2; }, l);
         }

         assert.deepEqual(functional.pipe2([ listadd1,
                                            listmultiply2,
                                            listadd1 ])(functional.range(1, 11)),
                          [ 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 ]);
    });
  });


  describe('#pipemaybe()', function() {
    const inc = function(v) {
      return v + 1;
    }

    const iseven = function(v) {
      if (v % 2 === 0)
        return v;
      else
        return null;
    }

    it('returns 3 for pipemaybe([ inc, inc, iseven, inc])(0)',
       function() {
         assert.equal(functional.pipemaybe([ inc,
                                             inc,
		                             iseven,
                                             inc ])(0),
                      3);
    });

    it('returns null for pipemaybe([ inc, inc, inc, iseven ])(0)',
       function() {
         assert.equal(functional.pipemaybe([ inc,
                                             inc,
		                             inc,
                                             iseven ])(0),
                      null);
    });
  });


  describe('#pipeeither()', function() {
    const inc = function(v) {
      return [null, v + 1];
    }

    const iseven = function(v) {
      if (v % 2 === 0)
        return [null, v];
      else
        return ['not even', v];
    }

    it('returns [null, 3] for pipeeither([ inc, inc, iseven, inc])(0)',
       function() {
         assert.deepEqual(functional.pipeeither([ inc,
                                                  inc,
		                                  iseven,
                                                  inc ])(0),
                          [null, 3]);
    });

    it('returns [\'not even\', 3] for pipeeither([ inc, inc, inc, iseven ])(0)',
       function() {
         assert.deepEqual(functional.pipeeither([ inc,
                                                  inc,
		                                  inc,
                                                  iseven ])(0),
                          ['not even', 3]);
    });
  });


  describe('#partial()', function() {
    it('returns [ 11..20 ] for map(partial(add, 10), range(1, 11))',
       function() {
         const add = function(a, b) {
           return a + b;
         }

         const add10 = function(x) {
           return add(x, 10);
         }

         assert.deepEqual(functional.map(add10,
                                         functional.range(1, 11)),
                          [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]);

         assert.deepEqual(functional.map(functional.partial(add, 10),
                                         functional.range(1, 11)),
                          [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]);
    });
  });


  describe('#curry()', function() {
    it('supports multiple execution paths',
       function() {
         const args = function(...a) {
           return a;
         }

         let cargs = functional.curry(args, 5);
         let cargsab = cargs('a')('b');

         assert.deepEqual(cargsab('c')('d')('e'),
                          [ 'a', 'b', 'c', 'd', 'e' ]);
         assert.deepEqual(cargsab('x')('y')('z'),
                          [ 'a', 'b', 'x', 'y', 'z' ]);
         assert.deepEqual(cargsab('c')('d')('e'),
                          [ 'a', 'b', 'c', 'd', 'e' ]);
         assert.deepEqual(cargsab('x')('y')('z'),
                          [ 'a', 'b', 'x', 'y', 'z' ]);
    });

    it('returns 15 for curry(add)(10)(5) and 25 for curry(add)(20)(5)',
       function() {
         const add = function(a, b) {
           return a + b;
         }

         let cadd = functional.curry(add);

         assert.equal(cadd(10)(5),
                      15);
         assert.equal(cadd(20)(5),
                      25);
    });

    it('returns [ 11..20 ] for map(curry(add)(10), range(1, 11))',
       function() {
         const add = function(a, b) {
           return a + b;
         }

         assert.deepEqual(functional.map(functional.curry(add)(10),
                                         functional.range(1, 11)),
                          [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]);
    });
  });


  describe('#factorial()', function() {
    it('returns [ 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800 ] for map(factorial, range(1, 11))',
       function() {
         assert.deepEqual(functional.map(functional.factorial,
                                         functional.range(1, 11)),
                          [ 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800 ]);
    });
  });


  describe('#fibonacci()', function() {
    it('returns [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ] for map(fibonacci, range(1, 11))',
       function() {
         assert.deepEqual(functional.map(functional.fibonacci,
                                         functional.range(1, 11)),
                          [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ]);
    });
  });


  describe('#memoizedfibonacci()', function() {
    it('returns 12586269025 for memoizedfibonacci(50)',
       function() {
         assert.equal(functional.memoizedfibonacci(50),
                      12586269025);
    });
  });


  describe('#tablefibonacci()', function() {
    it('returns 12586269025 for tablefibonacci(50)',
       function() {
         assert.equal(functional.tablefibonacci(50),
                      12586269025);
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
    it('returns false for ispalindrome(\'hello\')',
       function() {
         assert.equal(functional.ispalindrome('hello'),
                      false);
    });

    it('returns true for ispalindrome(\'detartrated\')',
       function() {
         assert.equal(functional.ispalindrome('detartrated'),
                      true);
    });

    it('returns true for ispalindrome(\'tattarrattat\')',
       function() {
         assert.equal(functional.ispalindrome('tattarrattat'),
                      true);
    });
  });
});
