""" 길이가 N인 수열 A에서 소수들을 골라 최소공배수 """

## set은 리스트 내 중복을 제거하는 것

N = int(input())
num_list = set([int(item) for item in input().split()])

result = 1

for n in num_list:
    if n > 1:
        for c in range(2, int(n**0.5) + 1):
            if n % c == 0:
                break
        else:
            result *= n

if result == 1:
    print("-1", end="")
else:
    print(result, end="")