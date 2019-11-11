import ast

if __name__ == "__main__":

    tree = ast.parse('def test(): print("TEST")')
    print(tree)
    print(ast.dump(tree))