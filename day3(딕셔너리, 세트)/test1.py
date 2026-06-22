'''
과제 1 — 딕셔너리

student = {"name": "최은관", "age": 19, "school": "스캐터랩대학교"}
이 딕셔너리로:

"name"의 값만 출력하기
"major"라는 key를 추가하고 값은 "AI"로 설정하기
"age"를 19에서 20으로 수정하기
.keys()와 .values() 각각 출력해서 어떤 게 나오는지 확인하기

'''

student = {"name": "최은관", "age": 19, "school": "대소고"}

## 1
print(student["name"])

## 2
student["major"] = "AI"
print(student)

## 3
student["age"] = 20

## 4
print(student.keys())
print(student.values())