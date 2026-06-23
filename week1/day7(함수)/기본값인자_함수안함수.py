'''

과제 2 — 기본값 인자 + 함수 안에 함수

# 1. 기본값 인자 (default argument)
# power(2, 3) → 8
# power(2)    → 4  (지수 기본값이 2)
def power(base, exp=2):
    # 짜보세요

# 2. 함수 안에서 다른 함수 호출
# 아래 두 함수를 활용해서 리스트에서 가장 큰 수의 제곱을 반환하는 함수를 짜세요
# 이미 짜둔 square()와 get_max()를 재활용하세요

numbers = [3, 7, 2, 9, 4]
# 기대 출력: 81  (가장 큰 수 9의 제곱)

def get_max_square(nums):
    # 힌트: for문으로 get_max 계속 갱신하고, 마지막에 square 적용
    # 짜보세요
get_max_square가 이번 핵심입니다. 함수를 부품처럼 조립해서 쓰는 구조 — PyTorch 코드 전체가 이 패턴입니다. 막히면 막힌 부분 그대로 가져오세요.

'''
numbers = [3, 7, 2, 9, 4]

def square(num):
    sq_num = num ** 2
    return sq_num


def get_max(a, b):
    if a > b:
        return a
    else:
        return b

## 1
def power(base, exp=2):
    powered_num = base ** exp
    return powered_num

## 2
def get_max_square(nums):
    max_val = nums[0]

    for i in nums:
        max_val = get_max(max_val, i)
    
    return square(max_val)


print(power(2, 3))
print(get_max_square(numbers))