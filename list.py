# 리스트 []

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

#다음 정류장에 하하가 탄다면?
subway.append("하하") # 뒤에 추가하기 
print(subway)

#정형돈을 유재석과 조세호 사이에 넣기
subway.insert(1, "정형돈") 
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇명 있는지 확인하기 
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5,3,6,2,7]
num_list.sort()
print(num_list)

#뒤집기
num_list.reverse()
print(num_list)

# 값 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형과 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5,3,6,2,7]
num_list.extend(mix_list)
print(num_list)