def plus(a, b):
    return a + b

def plus2(a, b):
    return int(a) + b

def minus(a, b):
    return a - b

def times(a, b):
    return a * b

def division(a, b):
    return a / b

def negation(a):
    return -a

def ms_pow(a, b):
    return a ** b

def remainder(a, b):
    return a % b

result = plus(b=2, a=5)
print(result)
result = minus(b=2, a=5)
print(result)
result = times(b=2, a=5)
print(result)
result = division(b=2, a=5)
print(result)
result = negation(5)
print(result)
result = ms_pow(b=2, a=5)
print(result)
print(pow(5,2))
result = remainder(b=2, a=5)
print(result)

result = plus2(b = 2, a="5")
print(result)