# for문 (반복문)
# print("대기번호 :  1")

# for waiting_no in [0,1,2,3,4]:
#   print("대기번호 : {0}" .format(waiting_no))

# for waiting_no in range(5): # 위 식과 동일함 0,1,2,3,4 / (1, 6) 이라고 적으면 1부터 6까지 출력
#   print("대기번호 : {0}" .format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#   print("{0}, 커피가 준비되었습니다. " .format(customer))

# while문 
# customer = "토르"
# index = 5
# while index >= 1:
#   print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요." .format(customer, index))
#   index -= 1
#   if index == 0:
#     print("커피는 폐기처분 되었습니다")

# customer = "아이언맨"
# index = 1
# while True:
#    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회" .format(customer, index))
#    index += 1
# 위 코드는 무한루프에 빠짐 

# customer = "토르"
# person ="Unknown"

# while person != customer:
#   print("{0}, 커피가 준비 되었습니다." .format(customer))
#   person = input("이름이 어떻게 되세요? ")

# absent = [2, 5]
# no_book = [7]
# for student in range(1, 11):
#   if student in absent:
#     continue
#   elif student in no_book:
#     print("오늘 수업 여기까지. {0}는 교무실로 따라와" .format(student))
#     break
#   print("{0}, 책을 읽어봐" .format(student))

students = [1,2,3,4,5]
print(students)
students = [i + 100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students] # 학생 이름을 길이로 변환
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students] #학생 이름을 대문자로 변환
print(students)

#quiz
# for 
# if 손님 in 소요시간:
#   print("매칭 되었습니다")
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): #승객
  time = randrange(5, 51)
  if 5 <= time <= 15: # 5분에서 15분 이내의 손님, 탑승 승객 수 증가 처리
    print("[O] {0}번째 손님 (소요시간 : {1}분)" .format(i, time))
    cnt += 1
  else: #매칭 실패
    print("[ ] {0}번째 손님 (소요시간 : {1}분)" .format(i, time))
  
print("총 탑승 승객 : {0} 분". format(cnt))
