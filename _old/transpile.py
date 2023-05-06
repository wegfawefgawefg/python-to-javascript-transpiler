import subprocess

# specify the path to the script and the file to parse
script_path = "./js_ast_to_js_code.js"
file_to_parse = "./output_ast.json"

# build the command to run the script
command = f"node {script_path} {file_to_parse}"

# use subprocess to run the command
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# check if the command executed successfully
if result.returncode == 0:
    # print the output of the script
    print(result.stdout)
else:
    # print the error message
    print(result.stderr)
