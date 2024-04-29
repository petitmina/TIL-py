# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다." .format(name))
# print("체력 {0}, 공격력 {1}\n" .format(hp, damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage =15


# print("{0} 유닛이 생성되었습니다." .format(tank_name))
# print("체력 {0}, 공격력 {1}\n" .format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage =15

# print("{0} 유닛이 생성되었습니다." .format(tank2_name))
# print("체력 {0}, 공격력 {1}\n" .format(tank_hp, tank2_damage))

# def attack(name, location, damage):
#   print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_name)
# attack(tank2_name, "1시", tank_name)

from random import *

# class
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print("{0} 유닛이 생성되었습니다." .format(name))

  def move(self, location):
    print("[지상 유닛 이동]")
    print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" .format(self.name, location, self.speed))

  def damaged(self, damage):
    print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
    self.hp -= damage
    print("{0} : 현재 체력은 {1} 입니다." .format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴되었습니다." .format(self.name))

    # self.damage = damage
    # print("{0} 유닛이 생성되었습니다." .format(self.name))
    # print("체력 {0}, 공격력 {1}\n" .format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank  = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}" .format(wraith1.name, wraith1.damage))

# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#    print("{0} 는 현재 클로킹 상태입니다." .format(wraith2.name))

# method

class AttackUnit(Unit):
  def __init__(self, name, hp, speed, damage):
    Unit.__init__(self, name, hp, speed)
    self.damage = damage

  def attack(self, location):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(self.name, location, self.damage))
  
#마린
class Marine(AttackUnit):
  def __init__(self):
    AttackUnit.__init__(self, "마린", 40, 1, 5)

  def stimpack(self):
    if self.hp > 10:
      self.hp -= 10
      print("{0} : 스팀팩을 사용합니다. (HP 10 감소)" .format(self.name))
    else:
      print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다." .format(self.name))

#탱크
class Tank(AttackUnit):
  seize_developed = False 

  def __init__(self):
    AttackUnit.__init__(self, "탱크", 150, 1, 35)
    self.seize_mode = False
  
  def set_seize_mode(self):
    if Tank.seize_developed == False:
      return
    
    if self.set_seize_mode == False:
      print("{0} : 시즈모드로 전환합니다." .format(self.name))
      self.damage *= 2
      self.seize_mode = True
    else:
      print("{0} : 시즈모드로 해제합니다." .format(self.name))
      self.damage / 2
      self.seize_mode = False

# firebat1 = AttackUnit("파이어뱃", 50, 10)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed =flying_speed

  def fly(self, name, location):
    print("{0} : {1} 방향으로 날아갑니다. [속도 {0}]" .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, 0, damage)
    Flyable.__init__(self, flying_speed)

  def move(self, location):
    self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
  def __init__(self):
    FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
    self.clocked = False

  def clocking(self):
    if self.clocked == True:
      print("{0} : 클로킹 모드 해제합니다." .format(self.name))
      self.clocked = False
    else: 
      print("{0} : 클로킹 모드 설정합니다." .format(self.name))
      self.clocked = True

def game_start():
  print("[알림] 새로운 게임을 시작합니다.")

def game_over():
  print("Player : gg")
  print("[Player] 님이 게임에서 퇴장하셨습니다.")

#실제 게임 진행
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t1)
attack_units.append(w1)

for unit in attack_units:
  unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
  if isinstance(unit, Marine):
    unit.stimpack()
  elif isinstance(unit, Tank):
    unit.set_seize_mode()
  elif isinstance(unit, Wraith):
    unit.clocking()

for unit in attack_units:
  unit.attack("1시")

for unit in attack_units:
  unit.damaged(randint(5, 21))

game_over()

# valkyrle = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrle.fly(valkyrle.name, "3시")

# vulture = AttackUnit("벌쳐", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

#pass
# class BuildingUnit(Unit):
#   def __init__(self, name, hp, location):
#     pass

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")



#super
# class BuildingUnit(Unit):
#   def __init__(self, name, hp, location):
#     #Unit.__init__(self, name, hp, 0)
#     super().__init__(name, hp, 0) # self 정보는 보내지 않기 
#     self.location = location