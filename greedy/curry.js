function curryN(fn, n) {
      // SOLUTION GOES HERE
  
  n = n || fn.length;

  return function rec(args, n) {
    if (n <= 1) {
      return fn(args); // i honestly don't understand this part -___-
    }
    return rec(fn.bind(this, args), n - 1);
  }

  // we just need to return a function that keeps partially applying our variables
}
    
module.exports = curryN