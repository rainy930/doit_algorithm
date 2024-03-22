""" 피제수(분자) A와 제수(분모) B가 있다. 두 수를 나누었을 때, 소숫점 아래 N번째 자리수를 구하시오 """

A, B, N = map(int, input().split(' '))

for i in range(N+1):
    ans = A //B
    A = A%B * 10
print(ans)