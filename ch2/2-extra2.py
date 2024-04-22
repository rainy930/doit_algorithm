""" 자연수 N부터 M까지 사이의 소수를 나열하기 """
# Hint : 에라토스테네스의 체

N, M = map(int, input().split(' '))
if N > 1 and M > 1 and N < M:
    print(f'N: {N}, M: {M}')
else:
    print('잘못 입력하셨습니다.')

L = [None] * (M - N)
ptr = 0

for i in range(N, M+1):
    erasto = int(i**(1/2))
    for j in range(2, erasto+1):
        if i % j == 0:
            break
    else: # for문이 break 등으로 중간에 빠져나오지 않고 끝까지 실행 됐을 경우
        L[ptr] = i
        ptr += 1

for p in range(ptr):
    print(L[p])