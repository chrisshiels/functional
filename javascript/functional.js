#!/usr/bin/env node

// 'functional.js'.
// Chris Shiels.


'use strict';


const _range = function(n, m = 0) {
  if (n == m)
    return [];
  else
    return _range(n - 1, m).concat(n - 1)
}


const _reverse = function(l) {
  if (l.length === 0)
    return [];
  else
    return _reverse(l.slice(1)).concat(l[0])
}
