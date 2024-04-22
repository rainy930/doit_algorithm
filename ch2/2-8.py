""" 1,000 이하의 소수를 나열하기 """

counter = 0

for n in range(2, 1001): # 1은 소수가 아니기에 제외
    for i in range(2, n): # 1과 자기 자신의 값 사이의 모든 정수에 대해 나누어 떨어지는 것을 파악
        counter += 1 # 연산 수 카운팅
        if n % i == 0: # 나머지가 0, 즉 나누어 떨어지면 중단
            break
    else:
        print(n) # for문이 break 등으로 중간에 빠져나오지 않고 끝까지 실행 됐을 경우
print(f'나눗셈을 실행한 횟수: {counter}')