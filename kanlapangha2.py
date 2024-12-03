class CircularQueue:
    def __init__(self, n):
        self.n = n
        self.queue = [] * n  
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if ((self.rear + 1) % self.n == self.front):  
            print('เพิ่มข้อมูลไม่ได้เพราะคิววงกลมเต็ม')
        elif (self.front == -1): 
            self.front = 0
            self.rear = 0
            self.queue.append(data)
        else: 
            self.rear = (self.rear + 1) % self.n
            self.queue.append(data)
    def dequeue(self):
        if (self.front == -1): 
            print('ลบข้อมูลไม่ได้เพราะคิวว่าง')
        elif (self.front == self.rear): 
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:  
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.n
            return temp


    def display(self):
        if self.front == -1:  
            print('แสดงข้อมูลไม่ได้')
        elif self.rear >= self.front: 
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=' ')
        else:  
            for i in range(self.front, self.n):
                print(self.queue[i], end=' ')
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=' ')
        print()  



n = int(input('โปรดระบุขนาดของ Q ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป: '))
while n < 5:
    n = int(input('โปรดระบุขนาดของ Q ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป: '))

q = CircularQueue(n)

while True:
    print('โปรดระบุทางเลือกในการดำเนินการ:')
    print('1. รับข้อมูล')
    print('2. ลบข้อมูลที่จัดเก็บใน Q วงกลม 1 ตัว')
    print('3. แสดงตัวเลขจำนวนเต็มที่มีค่าน้อยกว่า 150 ที่จัดเก็บในคิวทางจอภาพ')

    choice = input("ทางเลือกในการดำเนินการ: ")

    if choice == '1':
        data = input("รับข้อมูล: ")
        q.enqueue(data)
    elif choice == '2':
        result = q.dequeue()
        if result is not None:
            print("ลบข้อมูล 1 ตัว: {result}")
    elif choice == '3':
        print("แสดงข้อมูลที่มีค่าน้อยกว่า 150:")
        for item in q.queue:
            if isinstance(item, int) and item < 150:  
                print(item, end=' ')
        break

