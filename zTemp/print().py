# 문자 출력
print('Hello, Python !!')
print('반갑습니다. \n파이썬세계로 온것을 환영합니다.') # '\n' 은 줄바꿈
print("문자는 반드시 인용부호(' ' 혹은 \" \")로 감싸야 합니다.") # '\'는 명령 문자앞에 붙이면 그 문자를 그대로 문자로 출력

# 숫자 출력
print(100)
print(150 + 200)
print(150 - 200)

# 기본연산
x = 50
y = 4.

print("x = ", x)
print("y = ", y)
print("x + y = ", x+y)
print("x * y = ", x*y)
print("x / y = ", x/y)
print("-x = ", -x)
print("+x = ", +x)
print("x ** y = ", x**y)
print("pow(x,y) = ", pow(x, y))

# 변수에 문자담기
name = '홍길동'
greeting = '안녕'

print(name, greeting)
print(greeting, name)

text = name + '님, ' + greeting + '하세요'
print(text)

# 변수에 숫자담기
coffee1_name = '카페라떼'; coffee1_val = 4000;
coffee2_name = '카푸치노'; coffee2_val = 4500;
coffee3_name = '마끼야또'; coffee3_val = 5000;

# Case 1
# print('손님, ' + coffee1_name + coffee2_name + coffee3_name + '를 주문하셨습니다.')
# print('가격은 ' + coffee1_val + coffee2_val + coffee3_val + '원 입니다.')
# TypeError 발생

# Case 2
# print('손님, ' + coffee1_name + coffee2_name + coffee3_name + '를 주문하셨습니다.')
# print('가격은 ' + str(coffee1_val + coffee2_val + coffee3_val) + '원 입니다.')

# Case 3
coffee_val = coffee1_val + coffee2_val + coffee3_val
print('손님, \n%s, %s %s를 주문하셨습니다.' % (coffee1_name, coffee2_name, coffee3_name))
print('가격은 %d원 입니다.' % coffee_val)
