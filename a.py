import ast


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


# Example usage
source_code = """
def foo(x):
    return x + 1

foo(5)
"""

tree = ast.parse(source_code)
walker = ASTWalker(verbose=True)
walker.visit(tree)
