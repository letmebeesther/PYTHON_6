a=[1,2,3,4,5,6,7,8]
#   0 1 2 3 4 5 6 7 <= 인덱스 값
#  -8 -7 -6 -5 -4 -3 -2 -1 <= 인덱스 값

print('인덱스 값을 통한 원하는 요소 출력방법')
print('a[2:6] = ', a[2:6])  #인덱스 숫자임. 입력한 인덱스 사이의 숫자가 출력됨
print('a[3:] = ', a[3:]) #입력한 인덱스의 요소포함  끝까지 출력함
print('a[:5] = ', a[:5])  #입력한 인덱스의 요소포함 처음부터 출력함
print('a[:-2] = ', a[:-2]) 
print('a[-4:] = ', a[-4:])
print('a[-5:-2] = ', a[-5:-2])
print()

print('인덱스 입력한 반복문으로 원하는 요소 출력') #a[초기값:종료값:증가값]
print('a[1::2] = ', a[1::2])
print('a[1::3] = ', a[1::3])
print('a[2:6:2] = ', a[2:6:2])
print('a[::-1] = ', a[::-1])
print('a[::-2] = ', a[::-2])
print('a[::-3] = ', a[::-3])


