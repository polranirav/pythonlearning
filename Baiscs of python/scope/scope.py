username = "nirav polara"


def func():
    username = "nikhil"
    print(username)
print(username)
func()

x = 99


# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x
#     x = 12

# func3()
# print(x)


def f1():
    x = 88

    def f2():
        print(x)

    return f2


myResult = f1()
myResult()


def cod(num):
    def actual(x):
        return x ** num
    return actual


f = cod(2)
g = cod(2)

print(f(4))
print(g(3))