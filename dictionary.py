# 딕셔너리는 {key: value}로 표현함
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])

print(cabinet.get(3))
# print(cabinet[5]) 값이 없는경우에 프로그램 종료됨
# print(cabinet.get(5)) 값이 없는 경우에 none을 출력시킴
# print(cabinet.get(5, "사용가능")) 값이 없으면 뒤에값 실행시킴 
print("hi")

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#데이터 추가
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

#데이터 삭제
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

#모든 값 삭제
cabinet.clear()
print(cabinet)
