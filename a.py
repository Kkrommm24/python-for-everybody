#print("Nhap so tien:", end = " ")
#usd = int(input())
#vnd = usd * 22
#print(str(usd) + " USD = "  + str(vnd) + "k VND")

#PRINT
print('Website \'python.hung\' ')
print("Website \t python.hung")

guy = "Ban"
doamin = "python.hung"
full = "Chao mung %s den voi website %s" %(guy, doamin)
print(full)
# Chao mung Ban den voi website python.hung

#STRING
name = "Hoang Duc Gia Hung"
print(name[0]) # H
print(name[-1]) # g
print(name[17]) # g
print(name[0:18]) # lay tu 0 den (18 - 1)
print(name[14:]) # Hung
print(name[-4:]) # Hung

#NUMBER
age = 22
print(age) # 22

#del age # giai phong bo nho
#print(age)
# name 'age' is not defined

#LIST
name = ['Hoang Duc Gia Hung', 'Nguyen Van A', 'Nguyen Thi E']
print(name[0]) # Hoang Duc Gia Hung
print(name[1]) # Nguyen Van A
print(name[2]) # Nguyen Thi E
# hoặc
print(name[-3]) # Hoang Duc Gia Hung
print(name[-2]) # Nguyen Van A
print(name[-1]) # Nguyen Thi E

print(name[0:2]) # end - 1
# ['Hoang Duc Gia Hung', 'Nguyen Van A']
# hoặc
print(name[-3:-1])
# ['Hoang Duc Gia Hung', 'Nguyen Van A']

name[1] = 2003
print(name)
del name[2]
print(name)

option = [29,12,2003]
myList = ['HDGH', option]
print(myList)
# ['HDGH', [29,12,2003]]
subList = myList[1] # [29,12,2003]
subList[0] # 29
# hoặc có thể viết ngắn gọn như sau
myList[1][0] # 29

#TUPLE
day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
a = ()
b = (10,)
day[0] # monday
day[-2] # saturday
day[1:3] # ('tuesday', 'wednesday')
day[:3] # ('monday', 'tuesday', 'wednesday')
day[1:] # ('tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
# del day

day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday')
day3 = day1 + day2
print(day3)
# ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

#Dictionary
person = {
    'name': 'Hoang Duc Gia Hung',
    'age': 20,
    'male': True,
    'status': 'unknown'        
    }
person['name'] # Hoang Duc Gia Hung
person['status'] # unknown

person['status'] = 'married'
print(person)
del person['status']
print(person)
person.clear()
print(person)
#{}

person = {
    'name': 'Random Person',
    'option': {
                'age': 22,
                'male': True,
                'status': 'alone'
            }        
    }

print(person['option']['age'])
# 22