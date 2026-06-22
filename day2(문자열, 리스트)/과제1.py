'''

과제 1 — 문자열
다음 코드를 직접 작성해서 결과를 보여주세요:

- f-string으로 "제 이름은 OOO이고, 나이는 OO살입니다" 출력하기
- 문자열 슬라이싱: "ScatterLab"에서 "Scatter"만 잘라내기
- "hello world".upper(), .title(), .split() 각각 결과 확인하기

'''

## 1
name = "최은관"
age = 19
result = f"제 이름은 {name}이고, 나이는 {age}살입니다"
print(result)


## 2
company = "ScatterLab"
print(company[0:7])
print(company[7:])

## 3
hw = "hello world"

print(hw.upper())
## HELLO WORLD

print(hw.title())
## Hello World

print(hw.split())
## ['hello', 'world']
