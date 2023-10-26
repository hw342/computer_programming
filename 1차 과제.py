# 안전율(S)를 계산하는 함수
def calculate_safety_factor(strength, allowable_stress):
    safety_factor = strength / allowable_stress
    return safety_factor

# 사용자 입력 함수
def get_user_input(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("유효한 숫자를 입력하세요.")

# 메인 프로그램
if __name__ == "__main__":
    print("안전율 (S) 계산기")

    while True:
        # 기준강도와 허용응력을 입력받습니다.
        strength = get_user_input("기준강도를 입력하세요: ")
        allowable_stress = get_user_input("허용응력을 입력하세요: ")

        # 안전율을 계산하고 출력합니다.
        safety_factor = calculate_safety_factor(strength, allowable_stress)
        print(f"안전율 (S) = {safety_factor:.2f}")

        # 계속할지 사용자에게 물어봅니다.
        repeat = input("계속하시겠습니까? (y/n): ")
        if repeat.lower() != 'y':
            break
