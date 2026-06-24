'''

# 아래 클래스를 완성하세요

class Dog:
    # __init__: name과 age를 받아서 저장
    
    # bark(): "왈왈!" 출력
    
    # info(): "이름: OOO, 나이: OO살" 출력

# 완성 후 아래 코드가 동작해야 합니다
dog = Dog("초코", 3)
dog.bark()
dog.info()

'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print("왈왈!")
    
    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}살")

dog = Dog("초코", 3)
dog.bark()
dog.info()