""" 자연수 N 이하 소수를 나열하기 """

## 소수 : N의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않음

N = int(input())

prime = [None] * N
prime[0:2] = 2, 3
prime_idx = 2

for num in range(5, N+1, 2): ## 홀수만 처리
    idx = 0
    while prime[idx]*prime[idx] <= num:
        if num % prime[idx] == 0:
            break
        idx += 1
    else:
        prime[prime_idx] = num
        prime_idx += 1

print([num for num in prime if num is not None])