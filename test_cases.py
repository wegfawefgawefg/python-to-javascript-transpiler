def add(x, y):
    return x + y


add_target = """function add(x, y) {
        return x + y;
}"""


def more_ops(x, y):
    return x + y * 2


more_ops_target = """
function more_ops(x, y) {
  return x + y * 2;
}
"""


def abs_value(x):
    if x < 0:
        return -x
    else:
        return x


abs_value_target = """
function abs_value(x) {
  if (x < 0) {
    return -x;
  } else {
    return x;
  }
}
"""


def outer_function(x):
    def inner_function(y):
        return x * y

    return inner_function(x + 1)


outer_function_target = """
function outer_function(x) {
  function inner_function(y) {
    return x * y;
  }
  return inner_function(x + 1);
}
"""


def printtest():
    print(1)


printtest_target = """
function printtest() {
  console.log(1);
}
"""


def printvar(x):
    print(x)


printvar_target = """
function printvar(x) {
  console.log(x);
}
"""


def fortest(x):
    for i in range(1, x):
        return i


fortest_target = """
function fortest(x) {
  for (let i = 1; i < x; i++) {
    return i;
  }
}
"""


def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total


sum_of_squares_target = """
function sum_of_squares(n) {
  let total = 0;
  for (let i = 1; i <= n; i++) {
    total += i * i;
  }
  return total;
}
"""


def countdown(x):
    while x > 0:
        print(x)
        x -= 1
    print("Liftoff!")


countdown_target = """
function countdown(x) {
  while (x > 0) {
    console.log(x);
    x--;
  }
  console.log("Liftoff!");
}
"""


def reverse_list(lst):
    result = []
    for item in lst:
        result.insert(0, item)
    return result


reverse_list_target = """
function reverse_list(lst) {
  let result = [];
  for (let item of lst) {
    result.unshift(item);
  }
  return result;
}
"""


tests = [
    (add, add_target),
    # (more_ops, more_ops_target),
    # (abs_value, abs_value_target),
    # (outer_function, outer_function_target),
    # (printtest, printtest_target),
    # (printvar, printvar_target),
    # (fortest, fortest_target),
    # (sum_of_squares, sum_of_squares_target),
    # (countdown, countdown_target),
    # (reverse_list, reverse_list_target),
]
