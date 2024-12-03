class CircularQueue:
    def __init__(self, n):
        self.n = n  # ขนาดของคิว
        self.queue = [None] * n  # สร้างลิสต์ที่มีขนาด n
        self.front = -1  # ตัวชี้ตำแหน่งหน้า
        self.rear = -1  # ตัวชี้ตำแหน่งท้าย

    def enqueue(self, data):
        if ((self.rear + 1) % self.n == self.front):  # ตรวจสอบว่าเต็มหรือยัง
            print('Circular queue is full')
        elif self.front == -1:  # ถ้าคิวว่าง
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data  # ใส่ข้อมูลที่ตำแหน่ง rear
        else:
            self.rear = (self.rear + 1) % self.n  # วนกลับมาที่ตำแหน่งแรก
            self.queue[self.rear] = data  # ใส่ข้อมูลที่ตำแหน่ง rear

    def dequeue(self):
        if self.front == -1:  # คิวว่าง
            print('Circular queue is empty')
            return None
        elif self.front == self.rear:  # ถ้ามีแค่ 1 ตัวในคิว
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.n  # ย้ายตำแหน่งหน้า
            return temp

    def display(self):
        if self.front == -1:  # ถ้าคิวว่าง
            print('Circular queue is empty')
        elif self.rear >= self.front:  # ถ้าท้ายไม่กลับมาที่หน้า
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=' ')
        else:  # ถ้าท้ายกลับมาที่หน้า
            for i in range(self.front, self.n):
                print(self.queue[i], end=' ')
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=' ')
        print()  # เพิ่มบรรทัดใหม่หลังการแสดงข้อมูล


# รับขนาดของคิว
n = int(input('โปรดระบุขนาดของ Q ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป: '))
while n <= 5:
    n = int(input('โปรดระบุขนาดของ Q ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป: '))

q = CircularQueue(n)

while True:
    print('โปรดระบุทางเลือกในการดำเนินการ:')
    print('1. รับข้อมูล')
    print('2. ลบข้อมูลที่จัดเก็บใน Q วงกลม 1 ตัว')
    print('3. แสดงตัวเลขจำนวนเต็มที่มีค่าน้อยกว่า 150 ที่จัดเก็บในคิวทางจอภาพ')
    print('4. ออกจากโปรแกรม')

    choice = input("ทางเลือก (1-4): ")

    if choice == '1':
        data = input("รับข้อมูล: ")
        q.enqueue(data)
    elif choice == '2':
        result = q.dequeue()
        if result is not None:
            print(f"ลบข้อมูล 1 ตัว: {result}")
    elif choice == '3':
        print("แสดงข้อมูลที่มีค่าน้อยกว่า 150:")
        for item in q.queue:
            if isinstance(item, int) and item < 150:  # ตรวจสอบเป็นจำนวนเต็ม
                print(item, end=' ')
        print()  # บรรทัดใหม่
    elif choice == '4':
        break  # ออกจากลูป

