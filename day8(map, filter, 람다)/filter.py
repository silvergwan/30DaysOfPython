''''

과제:
numbers = [1, 2, 3, 4, 5]

# 2. filter로 짝수만 걸러낸 리스트 만들기
# 힌트: list(filter(함수, 리스트))

'''

numbers = [1, 2, 3, 4, 5]

def is_even(num):
    return num % 2 == 0

print(list(filter(is_even, numbers)))