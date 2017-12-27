#동전합산 서비스 프로그램
#동전의 갯수를 입력하면 동전의 총액을 계산해주는 프로그램
#작성자 : 문용호


print("동전합산 서비스에 오신 것을 환영합니다.")

coin500 = input("500원짜리는 몇개 입니까?")
while not coin500.isdigit() :
    print("양수또는 '0' 만 입력해주세요.")
    coin500 = input("500원짜리는 몇개 입니까?")

coin100 = input("100원짜리는 몇개 입니까?")
while not coin100.isdigit() :
    print("양수또는 '0' 만 입력해주세요.")
    coin100 = input("100원짜리는 몇개 입니까?")

coin50 = input("50원짜리는 몇개 입니까?")
while not coin50.isdigit() :
    print("양수또는 '0' 만 입력해주세요.")
    coin50 = input("50원짜리는 몇개 입니까?")

coin10 = input("10원짜리는 몇개 입니까?")
while not coin10.isdigit() :
    print("양수또는 '0' 만 입력해주세요.")
    coin10 = input("10원짜리는 몇개 입니까?")


total = 500 * int(coin500) + 100 * int(coin100) + 50 * int(coin50) + 10 * int(coin10)

print("\n손님의 동전은 총", total, "원입니다.")
print("저희 서비스를 이용해주셔서 감사합니다.")
print("또 들려주세요.")
