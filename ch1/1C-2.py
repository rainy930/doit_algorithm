""" 세 정수를 입력받아 중앙값 구하기 1 """

a, b, c = map(int, input().split())

# print(f'{a*b:2}')
d = a if c else b
print(d)
