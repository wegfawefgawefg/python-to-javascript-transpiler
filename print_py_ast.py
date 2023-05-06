"""
Playing with the python ast
"""

import ast
import inspect
from pprint import pprint


class ASTWalker(ast.NodeVisitor):
    def __init__(self, verbose=False):
        super().__init__()
        self.verbose = verbose

    def visit(self, node, indent=0):
        if self.verbose:
            print("  " * indent, ast.dump(node))
        else:
            print("  " * indent, type(node).__name__)

        for child in ast.iter_child_nodes(node):
            self.visit(child, indent + 1)


def print_walk_ast(code, verbose=False):
    tree = ast.parse(code)
    walker = ASTWalker(verbose)
    walker.visit(tree)


def forbidden(func):
    def wrapper(*args, **kwargs):
        raise Exception("This function is forbidden.")

    return wrapper


# @forbidden
def ex():
    a = 1 + 5
    b = 12 * a
    c = b / 4
    return c


def basic():
    return 4 + 5


def printer():
    print(5)


def otherthing():
    # all the way to 50
    return (
        1
        + 2
        + 3
        + 4
        + 5
        + 6
        + 7
        + 8
        + 9
        + 10
        + 11
        + 12
        + 13
        + 14
        + 15
        + 16
        + 17
        + 18
        + 19
        + 20
        + 21
        + 22
        + 23
        + 24
        + 25
        + 26
        + 27
        + 28
        + 29
        + 30
        + 31
        + 32
        + 33
        + 34
        + 35
        + 36
        + 37
        + 38
        + 39
        + 40
        + 41
        + 42
        + 43
        + 44
        + 45
        + 46
        + 47
        + 48
        + 49
        + 50
    )


def optimizedotherthing():
    return 1275


def countdown(x):
    while x > 0:
        print(x)
        x -= 1
    print("Liftoff!")


if __name__ == "__main__":
    code = inspect.getsource(countdown)
    print_walk_ast(code)

# dump bytecode of this file in shell without any debug info
# python -m dis main.py
