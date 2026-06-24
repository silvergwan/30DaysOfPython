'''

과제 1 — 기본 함수

아래 세 가지를 함수로 만드세요:

# 1. 숫자 하나를 받아서 제곱을 반환하는 함수
# 함수명: square

# 2. 두 숫자를 받아서 더 큰 값을 반환하는 함수
# 함수명: get_max

# 3. 리스트를 받아서 평균을 반환하는 함수 (sum() 이번엔 써도 됩니다)
# 함수명: get_average
세 함수 다 짜고, 각각 호출해서 결과까지 출력하세요.

print(square(5))        # 25
print(get_max(3, 9))    # 9
print(get_average([4, 7, 2, 9, 3]))  # 5.0

짜보세요.

'''

## 1
def square(num):
    sq_num = num ** 2
    return sq_num


## 2
def get_max(a, b):
    if a > b:
        return a
    else:
        return b


## 3

# 리스트 하나를 받음
def get_average(numbers):       
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

# 숫자를 여러 개 직접 넘길 때
def get_gaeverage(*args):
    total = sum(args)
    avg = total / len(args)
    return avg

print(square(5))
print(get_max(3, 9))
print(get_average([4, 7, 2, 9, 3]))
print(get_gaeverage(4, 7, 2, 9, 3))     # 이렇게 호출하는 경우