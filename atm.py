# 입금한 금액을 받는 변수 : deposit_amount
# 입금된 금액은 balcnce 변수에 추가되도록 코드를 작성해주세요
# 영수증에 다음 순서로 값이 들어가도록 코드를 만들어주세요 -> "입금", 입금 요청액 총액 순으로 데이터 넣어주세요
# 단, 영수증에 내역은 변경되지 않아야 하며 입금 또는 출금이 진행될때마다 이력이 기록됩니다.
# 영수증 변수는 : receipts

receipts = []
balance = 3000  #현재 잔액을 보여주세요

while True:
    print()
    num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료)")
    if num == '4':
        break
    if num == "1":
        deposit_amount = int(input("입금할 금액을 입력해주세요 : ")) 
        balance = balance + deposit_amount
        receipts.append(("입금", deposit_amount, balance))
        print(f"입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.")

print(f"서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.")