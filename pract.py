money = int(input("금액을 입력하세요: "))
drink = {1: 700, 2 : 800, 3: 1200}
drink_list = ['사이다', '콜라', '물']
number = int(input('마실 음료의 번호를 입력하세요: '))

print(f"{drink_list[number-1]}(이)가 나왔습니다. 덜컹. \
    잔돈 : {money - drink[number]}")
# if number == 1:
#     print(f"사이다. 잔돈: {money - drink[number]}")
# elif number == 2:
#     print("콜라. 잔돈: ")
# else:
#     print("물. 잔돈: ")