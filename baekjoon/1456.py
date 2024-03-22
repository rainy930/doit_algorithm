num_min, num_max = map(int, input().split())

print_cnt = 0
def prime_check(num):
    global print_cnt
    if num*num <= num_max:
        print_cnt += 1
        return prime_check(num*num)
    else:
        return -1

if num_min == 1:
    num_min = 2

for num in range(num_min, num_max + 1):    
    if num == 2:
        cnt = 2
        prime_check(num)
        continue
    if num % 2 == 0:  # 짝수는 2를 제외하고 소수가 될 수 없으므로 건너뜀
        continue
    for l in range(2, int(num**0.5)+1):
        if num % l == 0:
            break
    else:
        cnt = 2
        prime_check(num)
        
print(print_cnt)
