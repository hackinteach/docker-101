from sys import argv
try:
    a = int(argv[1])
    b = int(argv[2])
    print(f"Result: {a+b}")
except Exception as e:
    print("Usage python app.py <a: int> <b: int>")
    exit(-1)
