import ast

def parse_code(file_path):
    with open(file_path, "r") as f:
        code = f.read()
    
    tree = ast.parse(code) #ToDo: remove later

    print(ast.dump(tree, indent=4)) #ToDo: remove later

    return ast.parse(code)
