# 방법1
print("나는 %d살입니다." % 20)
print("나는 %s를 좋아해요." % "파이썬") # %s는 문자나 정수 상관없이 출력됨
print("Apple 은 %c로 시작해요." %"A")
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

#방법2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨간", age = 20))

#방법4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출 문자
print("백문이 불여일견\n백견이 불여일타") #\n은 줄바꿈

print("이것은 \"사과\" 입니다.")

#\\ : 문장 내에세 \로 바뀜
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭 효과
print("Red\tApple")

#quiz1

url = "http://naver.com"
my_str = url.replace("http://", "") #http://를 찾아서 빈칸으로 바꿈
my_str = my_str[:my_str.index(".")] # . 이후의 글자를 자름
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))