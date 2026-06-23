'''

과제:
numbers = [1, 2, 3, 4, 5]

# 1. map으로 모든 숫자를 제곱한 리스트 만들기
# 힌트: list(map(함수, 리스트))

'''
numbers = [1, 2, 3, 4, 5]

def square(num):
    sq_num = num ** 2
    return sq_num

print(list(map(square, numbers)))