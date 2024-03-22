""" M이상 N이하의 소수를 모두 출력 """

num_min, num_max = map(int, input().split())

if num_min == 1:
    num_min = 2

for num in range(num_min, num_max + 1):
    if num == 2:
        print(num)
        continue
    if num % 2 == 0:  # 짝수는 2를 제외하고 소수가 될 수 없으므로 건너뜀
        continue
    for l in range(2, int(num**0.5)+1):
            if num % l == 0:
                break
    else:
        print(num)