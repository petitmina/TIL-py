# 함수의 정의
def open_account():
  print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money):
  print("입금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance + money))
  return balance + money

def withdraw(balance, money):
  if balance >= money:
    print("출금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance - money))
    return balance - money
  else:
    print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다" .format(balance))
    return balance
  
def withdraw_night(balance, money):
  commission = 100
  return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 200)
print(balance)

commission, balance = withdraw_night(balance, 200)
print("수수료는 {0} 원이며, 잔액은 {1} 원입니다." .format(commission, balance))

#기본값
# def profile(name, age, main_lang):
#   print("이름 : {0}\t나이 : {1}\t 주 사용 언어: {2}" .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#같은 학교 같은 학년 같은 반 같은 수업.
# def profile(name, age=17, main_lang="파이썬"):
#   print("이름 : {0}\t나이 : {1}\t 주 사용 언어: {2}" .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# keyword
def profile(name, age, main_lang):
  print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

#가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#   print("이름 : {0}\t나이 :{1}\t" .format(name, age), end=" ")
#   print(lang1, lang2, lang3, lang4, lang5)
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin","Swift", "", "", "")

def profile(name, age, *language):
  print("이름 : {0}\t나이 :{1}\t" .format(name, age), end=" ")
  for lang in language:
    print(lang, end=" ")
  print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin","Swift")

#지역함수 전역함수
gun = 10 #전역 함수

# def checkpoint(soldiers):
#   global gun #전역공간에 있는 gun 사용
#   gun = gun - soldiers
#   print("[함수 내] 남은 총 : {0}" .format(gun))

def checkpoint_return(gun, soldiers):
  gun = gun - soldiers
  print("[함수 내] 남은 총 : {0}" .format(gun))
  return gun

print("전체 총 : {0}" .format(gun))
# checkpoint(2)
gun = checkpoint_return(gun, 2)
print("남은 총 : {0}" .format(gun))


#quiz
def std_weight(height, gender):
  if gender == "남자":
    return height * height * 22
  else:
    return  height * height * 21

height = 175 #  cm단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다." .format(height, gender, weight))