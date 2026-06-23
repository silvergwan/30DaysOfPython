''''

과제:
numbers = [1, 2, 3, 4, 5]

# 3. 위 두 개를 lambda로 다시 짜기
# 힌트: lambda x: x**2

'''

numbers = [1, 2, 3, 4, 5]

print(list(map(lambda x: x**2, numbers)))

print(list(filter(lambda x: x%2==0, numbers)))