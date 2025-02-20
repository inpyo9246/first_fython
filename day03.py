#fruits = ["apple" , "orange" , "banana"] # 문자열 리스트
#numbers = [4, 1, 5, 2 , 6] #숫자 리스트
#bols = [True , False , True] #불리언 리스트
#mixed_list = ["안녕하세요" , 12 , True]

#print(fruits[1][0])
#print(fruits[-2])

#fruits[1] = "cherry"
#print(fruits)

#numbers.append("hi") #요소 추가(마지막자리)
#print(numbers)
#numbers.insert(0,"2") #요소추가 원하는자리
#print(numbers)
#numbers.pop() # 요소 제거 마지막자리
#print(numbers)
#print(numbers.pop())# 요소 리턴
#print(numbers)
#numbers.remove(1)
#print(numbers)
#del numbers[1]
#rint(numbers)

#print(len(mixed_list)) #리스트길이
#print(numbers)
#fruits.sort()
#print(fruits)

#숫자 = [1,5,6]
#숫자.sort()
#print(숫자)
#숫자.sort(reverse=True) # 역순(기본이 Falss로 인식)
#print(숫자)

#numbers.reverse()
#print(numbers)
#numbers.sort()
#print(numbers)
#numbers.sort(reverse=True)
#print(numbers)

#fruits = "-".join(fruits)
#print(fruits)

#cart = []

#cart.append(input("추가할 상품 :"))
#cart.append(input("추가할 상품 :"))
#cart.append(input("추가할 상품 :"))

#print(cart)

#튜플

#튜플
colors = ("red", "green" , "black" , "yellow") #변경불가능
numbers = (1 , 5 , 3 , 9)
bools = (True , False , True)
mixed_tuple = ("red" , 1, True)

a=("first",) #요소가 하나일때는 마지막 쉼표.
print(colors[1])

#colors[1] = "yellow" #튜플은 변경불가.
print(numbers[0:2]) #슬라이싱 가능.
print(numbers.count(5))
print(numbers.index(1))

a, b , c , d = colors
print(a , b , c ,d)
print(c)


