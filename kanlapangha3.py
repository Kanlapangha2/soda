class Node:
    def __init__(self, info = None):
        self.info = info
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def AtTheBegining(self, data):
        if self.head != None:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode

    def AtTheEnd(self, data):
        if self.head == None:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.tail.next = NewNode
            self.tail = NewNode

    def display(self):
        if self.head is None:
            print("Linked list ว่าง")
            return
        
        print("ข้อมูลทั้งหมด:", end=" ")
        current = self.head
        while current:
            print(current.info, end=" ")
            current = current.next
        print()
    
    def calculate_average(self):
        if self.head is None:
            return 0
        
        total = 0
        count = 0
        current = self.head
        
        while current:
            total += current.info
            count += 1
            current = current.next
            
        return total / count


list = SLinkedList()

print("โปรดระบุทางเลือกในการดำเนินการกับSingly linked list")
print("B:เพิ่มข้อมูลที่จุดเริ่มต้น Singly linked list")
print("E:เพิ่มข้อมูลแบบต่อจากโหนดสุดท้ายของ Singly linked list")
soda = input("กรุณาเลือก B หรือ E: ")
while soda in ('B', 'E'):
    data = int(input("ป้อนข้อมูล: "))
    
    if soda == 'B':
        list.AtTheBegining(data)
    else:
        list.AtTheEnd(data)
    
    list.display()
    soda = input("กรุณาเลือก B หรือ E: ")

print("\nผลลัพธ์สุดท้าย:")
list.display()

if list.head:
    print(f"ข้อมูลที่ตำแหน่งทีพอยน์เดอร์ head: {list.head.info}")
    print(f"ข้อมูลที่ตำแหน่งที่พอยน์เดอร์ tail: {list.tail.info}")
    print(f"ค่าเฉลี่ยของข้อมูล: {list.calculate_average():.2f}")
else:
    print("ไม่มีข้อมูลใน Linked List")
