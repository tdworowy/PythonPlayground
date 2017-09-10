import ast

tree = ast.parse('def test(): print("TEST")')
print(tree)
print(ast.dump(tree))