# def say_hello(who):
#     print("hello", who)
# say_hello("yong")

def puls(a, b):
    print(a + b)

def minus(a, b=5):
    print(a - b)
# 파이썬 문구에선 function 안에서 값을 넣어줄수 있다
puls(2, 5)
minus(2)

def say_hello2(name="yong"):
    print("hello", name)
# 넘어오는 값이 없으면 yong 있으면 Kim
say_hello2()
say_hello2("Kim")
