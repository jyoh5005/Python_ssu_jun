class Circle:
    def __init__(self, radious):
        self.__radious = radious
    def __add__(self, other):
        return Circle(self.__radious + other.__radious)
    def __lt__(self, other):
        return self.__radious < other.__radious
    def __gt__(self, other):
        return self.__radious > other.__radious
    def __str__(self):
        return "원의 반지름은 %s입니다." % self.__radious

c1 = Circle(4)
c2 = Circle(5)
c3 = c1 + c2

print(c3)

if c1 < c2:
    print("c1 이 c2 보다 작습니다")
else:
     print("c1이 c2 보다 큽니다")

if c2 > c3:
    print("c2 이 c3 보다 큽니다")
else:
    print("c2 이 c3 보다 작습니다")
