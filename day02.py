print("Hello World")

name = "김인표"
age = 32.155
#print(name)
"제 이름은 ____입니다."
#print("제 이름은" + name + "입니다") #띄어쓰기 x
#print("제 이름은" , name , "입니다") #띄어쓰기 o

"제 나이는 __ 입니다."
#print("제 나이는" , age , "입니다.")
#print("제 나이는 {} 이고 이름은 {} 입니다.".format(age, name))
#print("제 나이는 {a} 이고 이름은 {b} 입니다.".format(a=32 , b="김인표"))
#print(f"제 나이는 {age} 이고 이름은 {name} 입니다.") #f-string 방식
#print("제 이름은 %s 입니다" % name) # 문자열로 들어간다.
#print("제 나이는 %d 입니다." % age) # 모든 숫자가 정수로 들어간다.
#print("제 나이는 %d 이고 이름은 %s 입니다." % (age , name))
#print("제 지분은 %d%% 입니다."%2)

#print("%10.2f" % 3.1415912548) #%"자릿수" ."몇번째소수점"


#입력
#emali = input("이메일 :")
#hobby = input("취미 :")
#address = input("주소 :")
#age = int(float(input("나이 : ")))
#print(f"제 이메일은{emali} 취미는 {hobby} 주소는 {address} 나이는{int(age)}")

a = "Life is too short, You need Python"
#print(a[2:10:2])
#date = "20250218sunny"
#date2 ="20260505cloudy"

#print(f"연도는 {date[:4]} 월은, {date[4:6]} 일은 ,{date[6:8]} , {date2[8:]}")

#print(len(a))#문자열 길이
#print(a.count("t" , 5 , 10))#문자가 몇 개있는지.
#print(a.index("t")) #앞에서 부터 찾는데 해당 문자의 인덱스 번호
#index는 없으면 오류를 낸다
#print(a.find("x"))# 문자열에만 사용가능
#find은 없으면 -1을 출력
#print(a.upper()) #lower 대문자/소문자
#print(a[0].isupper())
#print(a.replace("short", "long"))
#print(a.lstrip())#lstrip rstrip 문장기준 <l좌 r우> 공백삭제
#print(a.split())#공백 기준 리스트 형태로 배열

email = input("email : ")
#id는 ka5865@naver.com
#print(email.find("@") # =>index번호
email.index("@")
#print(email.split("@")[0])
