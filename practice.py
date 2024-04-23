# 애완동물을 소개해 주세요~

animal = "강아지"
name = "연탄"
age = 4
hobby = "산책"
is_adult = age >= 3

'''작은따옴표 3개는 주석 처리됨'''


print("우리집 " + animal + "의 이르은 " + name + "이예요")
hobby = "낮잠"
# , 는 띄워쓰기 , + int형은 str(int형)과 같음
print(name + "이는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") 
print(name + "이는 어른일까요? " + str(is_adult))

# quiz1
station = "사당"
print(station + "행 열차가 들어오고 있습니다")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다")

print(abs(-5)) #절댓값
print(pow(4, 2)) # 4의 2제곱 = 16
print(max(5, 12)) # 최대값을 찾아서 반환 / 결과는 12
print(min(5, 12)) # 최솟값을 찾아서 반환 / 결과는 5
print(round(2.33)) #반올림
print(round(2.99))

from math import * # 파이썬에서 제공하는 math library
print(floor(4.99)) # 내림 / 결과는 4
print(ceil(3.14)) #올림 / 결과는 4
print(sqrt(16)) # 제곱근 구하기 / 결과는 4

from random import * # 파이썬에서 제공하는 랜덤함수(난수)

print(random()) # 0.0 ~ 1.0 미만의 임의이 값 생성
print(random() * 10) #0.0  ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성

print(randrange(1, 45)) # 1 ~ 45 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

#quiz 2
# from random import * 원래는 선언해야함 위에 선언되어 있어서 생략
day = randint(4, 28)
day2 = randrange(4, 29)
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + " 일로 선정되었습니다")
print("오프라인 스터디 모임 날짜는 매월 " + str(day2) + " 일로 선정되었습니다")

#문자열

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """나는 소년이고 파이썬은 쉬워요 """

# 슬라이싱
idNum = "990120-1234567"

print("성별 : " + idNum[7])
print("연 : " + idNum[0:2]) # (index값이)0 부터 2 직전까지 
print("월 : " + idNum[2:4])
print("일 : " + idNum[4:6])

print("생년월일 : " + idNum[:6]) # idNum[0:6] 과 동일함
print("뒤 7자리 : " + idNum[7:])  # idNum[7: 14] 과 동일함
print("뒤 7자리 (뒤에부터) : " + idNum[-7:]) #맨 뒤에서 7번째부터 끝까지

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 두번째 n을 찾음
print(index)

print(python.find("Python"))

print(python.count("n")) # n이 총 몇 번 나오는지 알려줌

