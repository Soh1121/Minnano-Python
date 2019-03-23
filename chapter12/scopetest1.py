a = 1
b = 2
def foo():
    b = 10
    print(a, b)

foo()
print(a, b)
