import os
print("HAHA")
path = os.path.dirname(os.path.abspath(__file__))+ "\\script.py"
os.system("python < "+ path)
