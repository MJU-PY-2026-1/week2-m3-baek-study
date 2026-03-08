# 파일이름 :
# 작 성 자 :
americano_price = 4500
americano_count = 2
latte_price = 5000
latte_count = 1

# 2. 금액 계산
total_americano = americano_price * americano_count
total_latte = latte_price * latte_count
total_sum = total_americano + total_latte

# 3. 영수증 출력 (줄바꿈 필수!)
print("RECEIPT")
print("-" * 20)
print(f"아메리카노 x{americano_count} : {total_americano}원")
print(f"카페라떼 x{latte_count} : {total_latte}원")
print("-" * 20)
print(f"TOTAL : {total_sum}원")