import ast
import inspect
import json
from pprint import pprint
import textwrap
from print_py_ast import print_walk_ast
from pyast_to_jsast import convert_python_ast_to_js_ast
import subprocess
import test_cases


def test(show_ast_debug=False):
    # TODO: segregate errors for each part of transpilation
    js_ast_to_js_script_path = "./decomp_js_ast.js"
    for f, target in test_cases.tests:
        # print target function
        python_code = inspect.getsource(f)
        print(f"For Python function:\n\n{python_code}")

        try:
            python_ast = ast.parse(python_code)
            # print_walk_ast(python_ast)
            # print()
            js_ast = convert_python_ast_to_js_ast(python_ast)
            # dump to a file
            output_path = f"./transpiled_results/{f.__name__}.json"
            with open(f"./transpiled_results/{f.__name__}.json", "w") as f:
                json.dump(js_ast, f, indent=2)
            command = f"node {js_ast_to_js_script_path} {output_path}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{result.stdout}")

                if show_ast_debug:
                    # print the python ast, and the js ast
                    print("Python AST:\n")
                    print_walk_ast(python_ast, verbose=False)
                    node_str = ast.dump(python_ast)
                    print(node_str, end="\n\n")
                    print("JS AST:")
                    pprint(js_ast)
            else:
                print(f"Python Code:\n{python_code}")
                print(f"Failed to convert js ast to js code for {f} \n source: \n ")
                pprint(python_code)
                print(f"With error: \n ")
                pprint(result.stderr)

        except Exception as e:
            print(f"Error Converting ASTs {f.__name__}: {e}")
        print()


if __name__ == "__main__":
    test(show_ast_debug=True)
