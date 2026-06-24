'''

문제 1 — 함수가 함수를 반환합니다

# 곱셈기를 만드는 함수입니다
# make_multiplier(3)을 호출하면
# "3을 곱하는 함수"를 반환합니다

def make_multiplier(n):
    # 여기 안에 함수를 정의하고 반환하세요
    pass

# 완성 후 아래 코드가 동작해야 합니다
triple = make_multiplier(3)
print(triple(5))   # 15
print(triple(10))  # 30

double = make_multiplier(2)
print(double(7))   # 14

'''

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

triple = make_multiplier(3)
print(triple(5))   # 15
print(triple(10))  # 30

double = make_multiplier(2)
print(double(7))   # 14

'''

외부 함수 make_multiplier에 인자(배수)를 넘겨주면,
내부 함수 multiplier가 해당 값을 기억하여 입력된 수 x와 곱한 결과를 반환하는 구조입니다.

'''