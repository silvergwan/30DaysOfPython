'''

과제 1
score = 85
이 점수로 등급을 매기는 코드를 짜보세요:

90 이상: "A"
80 이상 90 미만: "B"
70 이상 80 미만: "C"
그 외: "F"

if / elif / else로 작성하고, 결과를 print()로 등급만 출력하세요.

'''

score = 85

if score >= 90:
    print("A")
    
elif score >= 80:
    print("B")

elif score >= 70:
    print("C")

else:
    print("F")

