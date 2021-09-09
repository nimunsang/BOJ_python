from os import error
from random import *

# ===========if===========

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("더워용")
# elif 10 <= temp < 30:
#     print("괜찮은 날씨에요")

# ========for========

# for waiting_no in range(5): # 0, 1, 2, 3, 4
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아아", "아바라", "모카"]
# for customers in starbucks:
#     print("{0}를 주문했습니당".format(customers))

# --------------for의 활용---------------

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# print(students)
# students = [len(i) for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# print(students)
# students = [i.upper() for i in students]
# print(students)

# from random import *
# passenger = randrange(5, 16)
# cnt = 0
# for i in range(50):
#     time = randrange(5, 51)
#     if(5 <= time <= 15):
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i+1, time))
#         cnt += 1
#     else:
#         print("[] {0}번째 손님 (소요시간 : {1}분".format(i+1, time))
    
# print("총 탑승 승객 : {0} 분".format(cnt))

# ============함수=============

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance, money): #입금
#     print("입금이 완료되었습니다. 잔액은 {0} 입니다.".format(balance +money))
#     return balance + money

# def withdraw(balance, money): #출금
#     if balance - money < 0:
#         print("잔액이 부족합니다.")
#         return balance
#     else:
#         print("출금이 완료되었습니다. 잔액은 {0} 입니다.".format(balance - money))
#         return balance - money

# def withdraw_night(balance, money): #저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission

# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# print(balance)
# balance = withdraw(balance, 1000)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원, 잔액 {1}원".format(commission, balance))

# def profile(name, age = 17, main_lang = "java"):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")
# profile("유재석")
# profile("고장맨")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("고장맨", 20, "python", "java", "c", "c++", "c#")

# def profile(name, age, *lang):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang)

# profile("고장맨", 20, "python", "java", "c", "c++", "c#")


# =============전역변수============

# gun = 10

# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# ===============퀴즈===============

# def std_weight(height, gender):
#     if gender == "male":
#         return round(height * height * 22 / 10000, 2)

#     else:
#         return float(height * height * 21 / 10000)

# height = int(input("키를 입력하세요: "))
# gender = input("성별을 입력하세요 : ")

# if(gender == "male"):
#     print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, std_weight(height, gender)))

# else:
#     print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, std_weight(height, gender)))

# ================표준입출력==============

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject, score)

# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for num in range(1, 3):
#     print("대기번호 : " + str(num).zfill(3))

# #빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간확보
# print("{0: >10}".format(500))
# #양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0:>+10}".format(-500))
# #왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# #3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000))
# #3자리 마다 콤마를 찍어주기, 부호도 붙이기
# print("{0:+,}".format(100000000))
# #3자리 마다 콤마를 찍어주기, 부호도 붙이기, 자릿수 확보하기
# print("{0:^>+15,}".format(100000000))
# #소수점 출력
# print("{0:.2f}".format(5/3))

# =============파일 입출력==============

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# print("코딩 : 100", file=score_file)
# score_file.write("과학 : 80")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) #줄별로 읽기, 한 줄 읽고 커서는 다음줄
# print(score_file.readline(), end="")
# print(score_file.readline())
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     # print(line, end="")
#     print(line[:2], end="")
# score_file.close()

# ==========pickle===========

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"고장맨", "나이":30, "취미":["잠, 코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이선을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# =============퀴즈============

# for i in range(1, 3):
#     with open("{0}주차.txt".format(i), "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -\n".format(i))
#         report_file.write("부서 : \n")
#         report_file.write("이름 : \n")
#         report_file.write("업무 요약 : \n")

# =============class 스타크래프트==============

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]"\
#             .format(self.name, location, self.damage))

# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# class Tank(AttackUnit):
#     seize_developed = False

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False
    
#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         if self.seize_mode == False:
#             self.seize_mode = True
#             self.damage *= 2
#             print("{0} : 시즈모드로 변환합니다.".format(self.name))

#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[player] 님이 게임에서 퇴장하셨습니다.")

# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# for unit in attack_units:
#     unit.move("1시")

# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# for unit in attack_units:
#     unit.attack("1시")

# for unit in attack_units:
#     unit.damaged(randint(5, 21))

# game_over()

# ===============퀴즈==============

# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print("주소 : {0}".format(self.location))
#         print("타입 : {0}".format(self.house_type))
#         print("거래타입 : {0}".format(self.deal_type))
#         print("가격 : {0}".format(self.price))
#         print("완공 : {0}".format(self.completion_year))

# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()

# ===============예외처리============

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 :"))
    
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
    
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하셨습니다.")
#     print(err)

# ===============에러 만들기============

# class BigNumberError(Exception): # 사용자 정의 예외처리
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
#         # raise ValueError
#     # print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하셨습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally: #에러와 상관없이 실행되는 문장 단, 정의된 에러만.(5, 0 넣어보기)
#     print("계산기를 이용해주셔서 감사합니다.")

# ===============퀴즈===================

# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

# class SoldOutError(Exception):
#     pass

# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까? "))
#         if not(order>=1):
#            raise ValueError 
        
#         if order > chicken: # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
            
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." \
#            .format(waiting, order))
#             waiting += 1
#             chicken -= order

#         if(chicken == 0):
#             raise SoldOutError

#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")

#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

# ============모듈================

# import theater_module

# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(2)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(2)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7) # error!!

# from theater_module import price_soldier as price
# price(5)      # 겹치면 이게 우선

# =================패키지==============

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import * # __init__ 에 초기화!
trip_to = vietnam.VietnamPackage()
trip_to.detail()