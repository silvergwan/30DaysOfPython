'''

과제 2

age = 17
has_ticket = True

age가 18 이상이거나(or), 18 미만이어도 has_ticket이 True면 입장 가능하다는 로직을 if문으로 짜고,
 입장 가능하면 "입장 가능", 아니면 "입장 불가"를 출력하세요.

'''

age = 17
has_ticket = True

if age >= 18 or has_ticket:
    print("입장 가능")
else:
    print("입장 불가")