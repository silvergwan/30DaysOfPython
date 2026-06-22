'''

과제 1 — for문 기본
numbers = [4, 7, 2, 9, 3]
이 리스트로:

for문으로 각 숫자를 2배로 만들어서 출력하기 (원본 리스트는 안 건드려도 됩니다, 그냥 출력만)
for문으로 전체 합을 구하기 (직접 누적 변수 만들어서 — sum() 함수 쓰지 말고)
for문 + if문 조합으로 짝수만 출력하기

'''

numbers = [4, 7, 2, 9, 3]
sum = 0

## 1
for i in range(len(numbers)):
    print(numbers[i]*2)

## 2
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)

## 3
for i in numbers:
    if i % 2 == 0:
        print(i)