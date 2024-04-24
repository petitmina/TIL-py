#튜플은 수정이나 추가가 불가
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# name ="김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 출력 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (자바나 파이썬을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (자바는 할 수 있지만 파이썬을 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# 파이썬을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# 자바를 잊어버림
java.remove("김태호")
print(java)

#자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

#quiz
from random import *
lst = [1,2,3,4,5]
users = range(1, 21) #1부터 20까지 생성
users = list(users)

winners = sample(users, 4)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))
print(" -- 축하합니다 -- ")