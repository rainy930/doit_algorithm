""" 유클리드 호제법으로 최대 공약수 구하기 """
cnt = 0
def gcd(x: int, y: int) -> int:
    global cnt
    cnt += 1
    print(f'{cnt} 수행 / x: {x} y: {y}')
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == '__main__':
    print('두 정숫값의 최대 공약수를 구합니다.')
    
    x = int(input('첫 번쨰 정숫값을 입력하세요.: '))
    y = int(input('두 번쨰 정숫값을 입력하세요.: '))
    
    print(f'두 정숫값의 최대 공약수는 {gcd(x,y)} 입니다.')
    

"""
1. 입력 받은 x, y 값에서 큰 값이 x로 오도록 조정
2. x를 y로 나누었을 때의 나머지를 계산
3. 만약 나머지가 0이 아니라면 4번 실행, 0이라면 종료
4. x, y 값에서 큰 값이 x로 오도록 조정
"""