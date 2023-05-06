/*
def add(x, y):
    return x + y
*/
function add(x, y) {
  return x + y;
}

/*
    def more_ops(x, y):
    return x + y * 2
*/
function more_ops(x, y) {
  return x + y * 2;
}

/*
    def abs_value(x):
    if x < 0:
        return -x
    else:
        return x
*/
function abs_value(x) {
  if (x < 0) {
    return -x;
  } else {
    return x;
  }
}

/*
        def outer_function(x):
    def inner_function(y):
        return x * y

    return inner_function(x + 1)
*/
function outer_function(x) {
  function inner_function(y) {
    return x * y;
  }
  return inner_function(x + 1);
}

/*
    def printtest():
    print(1)
*/
function printtest() {
  console.log(1);
}

/*
def printvar(x):
    print(x)
*/
function printvar(x) {
  console.log(x);
}

/*
def fortest(x):
    for i in range(1, x):
        return i
*/
function fortest(x) {
  for (let i = 1; i < x; i++) {
    return i;
  }
}

/*
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total
*/
function sum_of_squares(n) {
  let total = 0;
  for (let i = 1; i <= n; i++) {
    total += i * i;
  }
  return total;
}

/*
def countdown(x):
    while x > 0:
        print(x)
        x -= 1
    print("Liftoff!")
*/
function countdown(x) {
  while (x > 0) {
    console.log(x);
    x--;
  }
  console.log("Liftoff!");
}

/*
def reverse_list(lst):
    result = []
    for item in lst:
        result.insert(0, item)
    return result
*/
function reverse_list(lst) {
  let result = [];
  for (let item of lst) {
    result.unshift(item);
  }
  return result;
}
