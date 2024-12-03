def push_Stack (item, myStack):
    test = isFull(myStack)
    if test == 1:
        print('เพิ่มข้อมูลในstack')
    else:
        myStack.append(item)
def pop_Stack (myStack):
    test = isEmpty(myStack)
    if test == 1:
        print('ลบข้อมูลในstack')
    else:
        myStack.pop()
def isEmpty (myStack):
    if len(myStack) == 0:
        print('Stack is empty')
        return 1
    else:
        return 0
def isFull (myStack):
    if len(myStack)== n:
        print('Stack is full')
        return 1
    else:
        return 0
def display_Stack (myStack):
    test = isEmpty(myStack)
    if test == 1:
        print('Stack is empty')
    else:
        print(myStack)
def top_of_Stack (myStack):
    test = isEmpty(myStack)
    if test == 1:
        print('Stack is empty')
    else:
        print('Top of Stack = ', myStack[-1])
        
def cal_average(myStack):
    if  isEmpty(myStack):
        print('Stack ว่างไม่สามารถดำเนินการได้')
    else:
        avg=sum(myStack)/len(myStack)
        print('ค่าเฉลี่ยของข้อมุล myStack :(avg)')




n = int(input('โปรดระบุขนาดของ Stack ที่มีขนาดตั้งแต่6ช่องขึ้นไป='))
while n <6:
    n = int(input('โปรดระบุขนาดของ Stack ที่มีขนาดตั้งแต่6ช่องขึ้นไป='))
myStack=[]*n
print('โปรดระบุทางเลือกในการดำเนินการกับstack')
print('1:พิ่มข้อมูลในstack')
print('2:ลบข้อมูลในstack')
print('3:แสดงข้อมูลที่จัดเก็บในstack')
print('4:แสดงค่าเฉลี่ยข้อมูลที่จัดเก็บในstack')
d=int(input('ทางเลือกการดำเนินการ'))
while d == 1 or d == 2 or d == 3 or d == 4:
    if d == 1:
        item=float(input('โปรดระบุItem='))
        push_Stack (item,myStack)
    elif d == 2:
        pop_Stack(myStack)
    elif d == 3:
        display_Stack(myStack)
    elif d==4:
        cal_average(myStack)
  
        

              
