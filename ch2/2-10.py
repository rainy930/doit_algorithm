""" 1,000 이하의 소수를 나열하기(알고리즘 개선 2) """

counter = 0 # 곱셈, 나눗셈 실행 횟수를 나타내는 변수
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i]*prime[i] < n: 
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for l in range(ptr):
    print(prime[l])

print(f'소수 탐색 연산 수 : {counter}')
