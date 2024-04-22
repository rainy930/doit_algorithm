""" 1,000 이하의 소수를 나열하기(알고리즘 개선 1) """
# 소수는 2부터 n-1까지 어떤 소수로도 나누어 떨어지지 않는다.

counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2): 
    for i in range(1, ptr):
        counter += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 실행한 횟수: {counter}')