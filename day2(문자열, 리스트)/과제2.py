'''

과제 2 — 리스트
languages = ["Python", "Korean", "English"]
이 리스트로:

"Japanese" 추가하기 (append)
첫 번째 원소만 출력하기 (indexing)
마지막 두 개만 출력하기 (slicing)
for문으로 전체 출력하기

'''

languages = ["Python", "Korean", "English"]

## 1
languages.append("Japanese")
print(languages)

## 2
print(languages[0])

## 3
print(languages[-2:])


## 4
for i in range(len(languages)):
    print(languages[i])
