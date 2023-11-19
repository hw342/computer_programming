class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price


def main():
    # 음료 객체 미리 생성
    coffee = Beverage("커피", 3000)
    green_tea = Beverage("녹차", 2500)
    ice_tea = Beverage("아이스티", 3000)

    # 사용자 입력 받기 (첫 번째 입력)
    while True:
        selected_beverage = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")
        if selected_beverage in ["커피", "녹차", "아이스티"]:
            break
        else:
            print("올바른 음료를 선택해주세요.")

    # 선택한 음료에 따라 객체 할당
    if selected_beverage == "커피":
        beverage = coffee
    elif selected_beverage == "녹차":
        beverage = green_tea
    else:
        beverage = ice_tea

    # 사용자 입력 받기 (두 번째 입력)
    while True:
        try:
            quantity = int(input(f"{selected_beverage} 몇 잔 주문하시겠습니까? "))
            if quantity > 0:
                break
            else:
                print("잘못된 수량입니다. 1 이상의 수량을 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")

    # 주문 내역 출력
    total_price = beverage.calculate(quantity)
    print(f"\n주문 내역:\n{selected_beverage} {quantity}잔: {total_price}원")

if __name__ == "__main__":
    main()
